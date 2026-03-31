"""Output schema TypedDicts — matches the original JSON shape exactly."""

from __future__ import annotations
from typing import Optional, TypedDict


class PlayerImages(TypedDict):
    icon: str
    background: str


class PlayerInfo(TypedDict):
    name: str
    uid: str
    level: int
    images: PlayerImages


class PlayerStats(TypedDict):
    activeDays: int
    avatarNum: int
    achievementNum: Optional[int]
    chestNum: Optional[int]
    abyssProcess: Optional[str]


class StaminaReserve(TypedDict):
    amount: str
    full: bool


class StaminaStatus(TypedDict):
    amount: str
    recover: int           # seconds to full; 0 if already full
    reserve: Optional[StaminaReserve]  # HSR only


class DailyStatus(TypedDict):
    task: str
    extraReward: Optional[bool]


class RealtimeNotes(TypedDict):
    stamina: StaminaStatus
    expedition: str
    daily: DailyStatus
    weeklyBoss: str


class GameData(TypedDict):
    player: dict           # {info: PlayerInfo, stats: PlayerStats}
    realtime: RealtimeNotes


class HoyolabOutput(TypedDict):
    ts: int
    hkrpg: Optional[GameData]  # Honkai: Star Rail
    nap: Optional[GameData]    # Zenless Zone Zero
