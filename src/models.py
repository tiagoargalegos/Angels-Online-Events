from dataclasses import dataclass


@dataclass
class Event:
    id: str
    enabled: bool
    type: str
    name: str
    emoji: str
    color: int
    day: int
    summer_time: str
    winter_time: str