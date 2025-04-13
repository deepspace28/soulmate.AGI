# Phase 08: Daily Summary Generator
import json
from datetime import datetime

def generate_summary():
    entries = []
    with open("soulmate_memory.json") as f:
        for line in f:
            entries.append(json.loads(line.strip()))
    today = datetime.now().date().isoformat()
    daily = [e for e in entries if e["timestamp"].startswith(today)]
    return daily[-1] if daily else {"message": "No summary available."}