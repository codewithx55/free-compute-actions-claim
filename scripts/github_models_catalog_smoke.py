import json
import os
import urllib.error
import urllib.request


HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    "Content-Type": "application/json",
    "X-GitHub-Api-Version": "2026-03-10",
}


def request_json(url, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(url, data=data, headers=HEADERS, method="GET" if payload is None else "POST")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode(errors="replace")
        print(json.dumps({"status": "failed", "url": url, "http_status": error.code, "body": body[:700]}, indent=2))
        raise


def choose_models(catalog):
    text_models = [
        model for model in catalog
        if "text" in model.get("supported_input_modalities", [])
        and "text" in model.get("supported_output_modalities", [])
    ]
    preferred_needles = [
        "gpt-4o-mini",
        "gpt-4.1-mini",
        "Phi-4-mini",
        "phi-4-mini",
        "Llama",
        "llama",
    ]
    selected = []
    for needle in preferred_needles:
        for model in text_models:
            if needle in model["id"] or needle in model.get("name", ""):
                if model["id"] not in selected:
                    selected.append(model["id"])
                    break
        if len(selected) >= 3:
            return selected
    for model in text_models:
        if model["id"] not in selected:
            selected.append(model["id"])
        if len(selected) >= 3:
            break
    return selected


def run_inference(model_id):
    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": "Return compact JSON only."},
            {"role": "user", "content": f"Return {{\"secured\":true,\"model\":\"{model_id}\"}}."},
        ],
        "temperature": 0,
        "max_tokens": 80,
    }
    result = request_json("https://models.github.ai/inference/chat/completions", payload)
    return {
        "model": model_id,
        "response": result["choices"][0]["message"]["content"],
        "usage": result.get("usage", {}),
    }


def main():
    catalog = request_json("https://models.github.ai/catalog/models")
    selected = choose_models(catalog)
    if not selected:
        raise SystemExit("No text models found in GitHub Models catalog")
    results = []
    errors = []
    for model_id in selected:
        try:
            results.append(run_inference(model_id))
        except Exception as error:
            errors.append({"model": model_id, "error": repr(error)})
    if not results:
        raise SystemExit(f"No model inference calls succeeded: {errors}")
    print(json.dumps({
        "status": "secured",
        "surface": "github-models-catalog",
        "catalog_count": len(catalog),
        "models_attempted": selected,
        "models_succeeded": [item["model"] for item in results],
        "results": results,
        "errors": errors,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
