# Phase 04: Memory Logger
import json
from datetime import datetime

def log_memory(user_input, response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "response": response
    }
    with open("soulmate_memory.json", "a") as f:
        f.write(json.dumps(entry) + "\n")