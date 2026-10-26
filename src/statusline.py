"""Normalize service-health data for a status page."""
import json
from pathlib import Path
import sys

def normalize_status(value):
    normalized = str(value).strip().lower()
    return {"operational": "operational", "degraded": "degraded", "outage": "outage"}.get(normalized, "unknown")

def summarize(services):
    return [{"name": service["name"], "status": normalize_status(service.get("status", ""))} for service in services]

if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("fixtures/services.json")
    print(json.dumps(summarize(json.loads(source.read_text())), indent=2))
