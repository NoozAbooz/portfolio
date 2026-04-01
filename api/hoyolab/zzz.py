"""ZZZ (nap) data fetcher using genshin.py."""

from __future__ import annotations

import asyncio

import genshin

from hoyolab_types import GameData


async def fetch_zzz(client: genshin.Client, uid: int) -> GameData:
    """
    Fetch and normalise all ZZZ data for a given UID.

    Calls in parallel:
      - get_zzz_user        → career stats + avatar list
      - get_zzz_notes       → real-time notes (battery, dailies, etc.)
      - get_game_accounts   → nickname + level (not in get_zzz_user)
    """
    user_task    = asyncio.create_task(client.get_zzz_user(uid))
    note_task    = asyncio.create_task(client.get_zzz_notes(uid))
    account_task = asyncio.create_task(client.get_game_accounts())

    user, note, accounts = await asyncio.gather(user_task, note_task, account_task)

    # ── Nickname + level from game accounts ──────────────────────────────────
    # ZZZUserStats has no nickname/level; those live in the GenshinAccount entry.
    zzz_account = next(
        (a for a in accounts if a.game == genshin.Game.ZZZ and a.uid == uid),
        None,
    )
    name  = zzz_account.nickname if zzz_account else "Unknown"
    level = zzz_account.level    if zzz_account else 0

    # ── Player info ──────────────────────────────────────────────────────────
    player_info = {
        "name":  name,
        "uid":   str(uid),
        "level": level,
        "images": {
            "icon":       user.in_game_avatar,  # cur_head_icon_url
            "background": user.in_game_data.card_url,  # namecard URL
        },
    }

    # ── Career stats ─────────────────────────────────────────────────────────
    # ZZZStats: active_days, character_num (avatarNum), shiyu_defense_frontiers,
    #           bangboo_obtained, achievement_count, inter_knot_reputation
    s = user.stats
    player_stats = {
        "activeDays":     s.active_days,
        "avatarNum":      s.character_num,
        "achievementNum": s.achievement_count,
        "chestNum":       None,               # no chest count in ZZZ
        "abyssProcess":   s.inter_knot_reputation or None,
    }

    # ── Battery charge ────────────────────────────────────────────────────────
    # BatteryCharge: current, max, seconds_till_full
    bat = note.battery_charge
    battery_full = bat.current >= bat.max
    recover_secs = 0 if battery_full else bat.seconds_till_full

    stamina = {
        "amount":  f"{bat.current}/{bat.max}",
        "recover": recover_secs,
        # ZZZ has no reserve stamina
    }

    # ── Engagements (vitality) ────────────────────────────────────────────────
    # ZZZEngagement: current, max  — the daily engagement cap
    eng = note.engagement
    daily = {
        "task":       f"{eng.current}/{eng.max}",
        "extraReward": note.scratch_card_completed,  # daily card sign
    }

    # ── Bounty commission (weekly boss equivalent) ────────────────────────────
    # BountyCommission: cur_completed, total
    # hollow_zero.bounty_commission may be None if Hollow Zero is locked.
    bc = note.hollow_zero.bounty_commission
    if bc is not None:
        weekly_boss = f"{bc.cur_completed}/{bc.total}"
    else:
        weekly_boss = "0/0"

    # ZZZ has no expedition system
    expedition = "N/A"

    realtime: dict = {
        "stamina":    stamina,
        "expedition": expedition,
        "daily":      daily,
        "weeklyBoss": weekly_boss,
    }

    return {
        "player":  {"info": player_info, "stats": player_stats},
        "realtime": realtime,
    }
