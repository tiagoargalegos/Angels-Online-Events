import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = ROOT / "data" / "events.json"


def load_events():
    """Carrega todos os eventos ativos."""

    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [
        event
        for event in data["events"]
        if event["enabled"]
    ]


def get_event(event_id):
    """Obtém um evento pelo ID."""

    for event in load_events():

        if event["id"] == event_id:
            return event

    return None