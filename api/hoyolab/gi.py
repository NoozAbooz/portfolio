"""Genshin Impact (gi) data fetcher using genshin.py."""

from __future__ import annotations

import asyncio
from datetime import timedelta

import genshin

from hoyolab_types import GameData


def _pick_attr(obj: object, *names: str, default=None):
    for name in names:
        if hasattr(obj, name):
            value = getattr(obj, name)
            if value is not None:
                return value
    return default


def _seconds(value: object) -> int:
    if value is None:
        return 0
    if isinstance(value, timedelta):
        return int(value.total_seconds())
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return 0


def _namecard_background(user: object) -> str:
    namecard = _pick_attr(user, "namecard", "card", default=None)
    if namecard is None:
        return ""

    return _pick_attr(
        namecard,
        "banner",
        "background",
        "image",
        "url",
        default="",
    ) or ""


async def fetch_gi(client: genshin.Client, uid: int) -> GameData:
    """
    Fetch and normalize all Genshin data for a given UID.

    Calls in parallel:
      - get_genshin_user   -> player info + profile stats
      - get_genshin_notes  -> real-time notes (resin, commissions, etc.)
    """
    user_task = asyncio.create_task(client.get_genshin_user(uid))
    note_task = asyncio.create_task(client.get_genshin_notes(uid))
    account_task = asyncio.create_task(client.get_game_accounts())

    user, note, accounts = await asyncio.gather(user_task, note_task, account_task)

    gi_account = next(
        (a for a in accounts if a.game == genshin.Game.GENSHIN and a.uid == uid),
        None,
    )

    info = _pick_attr(user, "info", default=user)
    stats = _pick_attr(user, "stats", default=user)

    player_info = {
        "name": _pick_attr(gi_account, "nickname", default=None)
        or _pick_attr(info, "nickname", "name", default="Traveler"),
        "uid": str(uid),
        "level": int(
            _pick_attr(gi_account, "level", default=None)
            or _pick_attr(info, "level", "adventure_rank", default=0)
            or 0
        ),
        "images": {
            "icon": _pick_attr(
                gi_account,
                "icon",
                "avatar_url",
                default="",
            )
            or _pick_attr(
                user,
                "profile_picture",
                "in_game_avatar",
                default="",
            )
            or _pick_attr(info, "profile_picture", "icon", "avatar", default="")
            or "",
            "background": _namecard_background(user),
        },
    }

    chest_num = _pick_attr(stats, "chest_num", "chest_number", default=None)

    if chest_num is None:
        common_chests = int(_pick_attr(stats, "common_chests", "common_chest_number", default=0) or 0)
        exquisite_chests = int(_pick_attr(stats, "exquisite_chests", "exquisite_chest_number", default=0) or 0)
        precious_chests = int(_pick_attr(stats, "precious_chests", "precious_chest_number", default=0) or 0)
        luxurious_chests = int(_pick_attr(stats, "luxurious_chests", "luxurious_chest_number", default=0) or 0)
        remarkable_chests = int(_pick_attr(stats, "remarkable_chests", "remarkable_chest_number", "magic_chest_number", default=0) or 0)
        total_chests = (
            common_chests
            + exquisite_chests
            + precious_chests
            + luxurious_chests
            + remarkable_chests
        )
        chest_num = total_chests if total_chests > 0 else None

    abyss_process = _pick_attr(stats, "spiral_abyss", "abyss_process", default=None)

    player_stats = {
        "activeDays": int(_pick_attr(stats, "active_days", "active_day_number", default=0) or 0),
        "avatarNum": int(_pick_attr(stats, "characters", "avatar_num", "avatar_number", "character_number", default=0) or 0),
        "achievementNum": int(_pick_attr(stats, "achievements", "achievement_num", "achievement_number", default=0) or 0),
        "chestNum": chest_num,
        "abyssProcess": abyss_process,
    }

    current_resin = int(_pick_attr(note, "current_resin", "current_stamina", default=0) or 0)
    max_resin = int(_pick_attr(note, "max_resin", "max_stamina", default=160) or 160)
    resin_full = current_resin >= max_resin

    stamina = {
        "amount": f"{current_resin}/{max_resin}",
        "recover": 0
        if resin_full
        else _seconds(
            _pick_attr(
                note,
                "remaining_resin_recovery_time",
                "resin_recovery_time",
                "stamina_recover_time",
                default=0,
            )
        ),
    }

    expeditions = _pick_attr(note, "expeditions", default=()) or ()
    current_expedition = len(expeditions)
    total_expedition = int(_pick_attr(note, "max_expeditions", "max_expedition_num", "total_expedition_num", default=0) or 0)
    expedition = f"{current_expedition}/{total_expedition}" if total_expedition > 0 else "0/0"

    finished_commissions = int(
        _pick_attr(
            note,
            "finished_commissions",
            "completed_commissions",
            "completed_task_num",
            default=0,
        )
        or 0
    )
    total_commissions = int(_pick_attr(note, "total_commissions", "max_commissions", default=4) or 4)

    daily = {
        "task": f"{finished_commissions}/{total_commissions}",
        "extraReward": bool(
            _pick_attr(
                note,
                "claimed_commission_reward",
                "is_extra_task_reward_received",
                default=False,
            )
        ),
    }

    max_weekly = int(_pick_attr(note, "max_resin_discounts", default=3) or 3)
    remaining_weekly = int(_pick_attr(note, "remaining_resin_discounts", default=max_weekly) or max_weekly)
    used_weekly = max_weekly - remaining_weekly
    weekly_boss = f"{used_weekly}/{max_weekly}" if max_weekly > 0 else "0/0"

    realtime: dict = {
        "stamina": stamina,
        "expedition": expedition,
        "daily": daily,
        "weeklyBoss": weekly_boss,
    }

    return {
        "player": {"info": player_info, "stats": player_stats},
        "realtime": realtime,
    }
