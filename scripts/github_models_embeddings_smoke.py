import json
import os
import urllib.error
import urllib.request


def request_json(url, payload):
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2026-03-10",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode(errors="replace")
        print(json.dumps({"status": "failed", "http_status": error.code, "body": body[:700]}, indent=2))
        raise


def main():
    payload = {
        "model": "openai/text-embedding-3-small",
        "input": [
            "free compute secured",
            "github models embeddings proof",
            "vector search for incubator inventory",
        ],
    }
    result = request_json("https://models.github.ai/inference/embeddings", payload)
    vectors = result["data"]
    dimensions = len(vectors[0]["embedding"])
    print(json.dumps({
        "status": "secured",
        "surface": "github-models-embeddings",
        "model": payload["model"],
        "inputs": len(payload["input"]),
        "vectors": len(vectors),
        "dimensions": dimensions,
        "usage": result.get("usage", {}),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
