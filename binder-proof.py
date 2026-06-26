import json
import platform
import time

proof = {
    "status": "secured",
    "surface": "mybinder-runtime-python",
    "platform": platform.platform(),
    "python": platform.python_version(),
    "created_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

print(json.dumps(proof, sort_keys=True))
