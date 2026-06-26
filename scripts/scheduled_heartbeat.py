import hashlib
import json
import os
import platform
import time


def main():
    started = time.time()
    payload = {
        "status": "secured",
        "surface": "github-actions-scheduled-compute",
        "event": os.environ.get("GITHUB_EVENT_NAME"),
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "runner_os": os.environ.get("RUNNER_OS"),
        "runner_arch": os.environ.get("RUNNER_ARCH"),
        "python": platform.python_version(),
        "timestamp_unix": int(started),
    }
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    payload["digest_prefix"] = digest[:16]
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

