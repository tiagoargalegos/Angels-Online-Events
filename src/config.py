"""
config.py
----------

Carrega e valida o ficheiro data/settings.json.

Autor: AO Event Notifier
"""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = ROOT / "data"
SETTINGS_FILE = DATA_FOLDER / "settings.json"


class Config:

    def __init__(self):

        if not SETTINGS_FILE.exists():
            raise FileNotFoundError(
                f"Não foi encontrado: {SETTINGS_FILE}"
            )

        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            self.settings = json.load(f)

        self.validate()

    def validate(self):

        required = [

            "timezone",

            "minutes_before",

            "daily_summary",

            "summary_time",

            "language"

        ]

        missing = []

        for item in required:

            if item not in self.settings:
                missing.append(item)

        if missing:

            raise ValueError(
                f"Faltam configurações em settings.json: {', '.join(missing)}"
            )

    @property
    def timezone(self):
        return self.settings["timezone"]

    @property
    def minutes_before(self):
        return self.settings["minutes_before"]

    @property
    def daily_summary(self):
        return self.settings["daily_summary"]

    @property
    def summary_time(self):
        return self.settings["summary_time"]

    @property
    def language(self):
        return self.settings["language"]


config = Config()