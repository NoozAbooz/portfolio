"""HSR (hkrpg) data fetcher using genshin.py."""

from __future__ import annotations

import genshin

from hoyolab_types import GameData


async def fetch_hsr(client: genshin.Client, uid: int) -> GameData:
    """
    Fetch and normalise all HSR data for a given UID.

    Calls in parallel:
      - get_starrail_user  → player info + career stats
      - get_starrail_notes → real-time notes (stamina, dailies, etc.)
    """
    import asyncio

    user_task = asyncio.create_task(client.get_starrail_user(uid))
    note_task = asyncio.create_task(client.get_starrail_notes(uid))

    user, note = await asyncio.gather(user_task, note_task)

    # ── Player info ──────────────────────────────────────────────────────────
    # StarRailUserStats.info  →  StarRailUserInfo
    #   .nickname, .level, .avatar (head icon URL)
    # StarRailUserStats.in_game_avatar  →  alternative head icon URL
    # StarRailUserStats.phone_background  →  profile background URL

    info = user.info
    player_info = {
        "name": info.nickname,
        "uid": str(uid),
        "level": info.level,
        "images": {
            "icon": user.in_game_avatar,          # cur_head_icon_url
            "background": user.phone_background,  # phone_background_image_url
        },
    }

    # ── Career stats ─────────────────────────────────────────────────────────
    # StarRailStats: active_days, avatar_num, achievement_num,
    #                chest_num, abyss_process
    s = user.stats
    player_stats = {
        "activeDays":     s.active_days,
        "avatarNum":      s.avatar_num,
        "achievementNum": s.achievement_num,
        "chestNum":       s.chest_num,
        "abyssProcess":   s.abyss_process or None,
    }

    # ── Stamina ───────────────────────────────────────────────────────────────
    # stamina_recover_time is a timedelta; total_seconds() gives seconds to full.
    stamina_full = note.current_stamina >= note.max_stamina
    recover_secs = 0 if stamina_full else int(note.stamina_recover_time.total_seconds())

    stamina = {
        "amount":  f"{note.current_stamina}/{note.max_stamina}",
        "recover": recover_secs,
        "reserve": {
            "amount": f"{note.current_reserve_stamina}/2400",
            "full":   note.is_reserve_stamina_full,
        },
    }

    # ── Expeditions ───────────────────────────────────────────────────────────
    # accepted_expedition_num (field has a typo in the raw API; genshin.py corrects it)
    expedition = f"{note.accepted_expedition_num}/{note.total_expedition_num}"

    # ── Daily training ────────────────────────────────────────────────────────
    daily = {
        "task": f"{note.current_train_score}/{note.max_train_score}",
    }

    # ── Weekly boss (Echo of War) ─────────────────────────────────────────────
    # remaining_weekly_discounts counts DOWN from max; invert to show used/max.
    boss_used = note.max_weekly_discounts - note.remaining_weekly_discounts
    weekly_boss = f"{boss_used}/{note.max_weekly_discounts}"

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
