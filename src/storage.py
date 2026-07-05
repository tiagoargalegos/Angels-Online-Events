import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STATE_FILE = ROOT / "data" / "state.json"


def load_state():

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)