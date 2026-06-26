import json
import platform


print(json.dumps({
    "status": "secured",
    "surface": "github-actions-container-build-ghcr",
    "python": platform.python_version(),
    "platform": platform.platform(),
}, sort_keys=True))

