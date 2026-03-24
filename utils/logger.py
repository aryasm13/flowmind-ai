import json
from datetime import datetime

LOG_FILE = "data/logs.json"

def log_step(step, data):
    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append({
            "timestamp": str(datetime.now()),
            "step": step,
            "data": data
        })
        f.seek(0)
        json.dump(logs, f, indent=2)