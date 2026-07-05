"""
timezone.py
------------

Gestão de fusos horários para Portugal.

Deteta automaticamente se Portugal está em horário
de verão ou inverno.

Autor: AO Event Notifier
"""

from datetime import datetime
from zoneinfo import ZoneInfo

PORTUGAL = ZoneInfo("Europe/Lisbon")


def now():
    """
    Hora atual em Portugal.
    """
    return datetime.now(PORTUGAL)


def is_summer_time():

    """
    True se Portugal estiver em horário de verão.
    """

    return bool(now().dst())


def current_timezone():

    if is_summer_time():
        return "SUMMER"

    return "WINTER"


def event_time(event):

    """
    Recebe um evento e devolve a hora correta
    dependendo da época do ano.
    """

    if current_timezone() == "SUMMER":
        return event["summer_time"]

    return event["winter_time"]


def weekday():

    """
    Domingo
    Segunda
    etc...
    """

    return now().strftime("%A")


def current_time():

    """
    HH:MM
    """

    return now().strftime("%H:%M")