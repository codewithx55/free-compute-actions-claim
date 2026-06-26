import hashlib
import json
import os
import platform
import time


def main():
    started = time.time()
    digest = "seed"
    for index in range(200_000):
        digest = hashlib.sha256(f"{digest}:{index}".encode()).hexdigest()
    elapsed = time.time() - started
    payload = {
        "status": "secured",
        "surface": "github-actions-public-standard-runner",
        "runner_os": os.environ.get("RUNNER_OS"),
        "runner_arch": os.environ.get("RUNNER_ARCH"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "python": platform.python_version(),
        "machine": platform.machine(),
        "benchmark_seconds": round(elapsed, 4),
        "digest_prefix": digest[:16],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

