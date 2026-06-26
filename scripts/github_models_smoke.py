import json
import os
import urllib.error
import urllib.request


def main():
    token = os.environ["GITHUB_TOKEN"]
    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Return compact JSON only.",
            },
            {
                "role": "user",
                "content": "Return {\"free_compute\":\"secured\",\"surface\":\"github-models\",\"proof\":true}.",
            },
        ],
        "temperature": 0,
        "max_tokens": 80,
    }
    request = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode(errors="replace")
        print(json.dumps({"status": "failed", "http_status": error.code, "body": body[:500]}, indent=2))
        raise

    content = result["choices"][0]["message"]["content"]
    print(json.dumps({
        "status": "secured",
        "surface": "github-models",
        "model": payload["model"],
        "response": content,
        "usage": result.get("usage", {}),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
