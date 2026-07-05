import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"

EVENTS = DATA / "events.json"

STATE = DATA / "state.json"


def load_events():

    with open(EVENTS, encoding="utf8") as f:
        return json.load(f)


def save_events(events):

    with open(EVENTS, "w", encoding="utf8") as f:

        json.dump(events, f, indent=4, ensure_ascii=False)


def load_state():

    with open(STATE, encoding="utf8") as f:
        return json.load(f)


def save_state(state):

    with open(STATE, "w", encoding="utf8") as f:

        json.dump(state, f, indent=4, ensure_ascii=False)