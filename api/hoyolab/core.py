"""
Hoyolab data aggregator — HSR + ZZZ + GI
Uses genshin.py (https://github.com/seriaati/genshin.py)

Usage:
    python main.py

Required environment variables:
    HOYO_COOKIE   Full cookie string from hoyolab.com DevTools
                  e.g. "ltoken_v2=...; ltuid_v2=..."
    HSR_UID       Your Honkai: Star Rail UID  (omit to skip)
    ZZZ_UID       Your Zenless Zone Zero UID  (omit to skip)
    GI_UID        Your Genshin Impact UID      (omit to skip)
"""

from __future__ import annotations

import asyncio
import json
import os
import time

import genshin

from gi import fetch_gi
from hsr import fetch_hsr
from zzz import fetch_zzz


async def get_hoyolab_data(
    cookie: str,
    hsr_uid: int | None = None,
    zzz_uid: int | None = None,
    gi_uid: int | None = None,
) -> dict:
    """
    Build a single unified payload for all configured games.

    Games with no UID are silently skipped.
    If one game fails, the error is logged and the other still resolves.
    """
    # genshin.py handles DS headers, cookie auth, and routing automatically.
    client = genshin.Client(cookie, game=genshin.Game.STARRAIL)

    output: dict = {"ts": int(time.time() * 1000)}
    jobs = []

    if hsr_uid:
        async def _hsr():
            try:
                output["hkrpg"] = await fetch_hsr(client, hsr_uid)
            except Exception as e:
                print(f"[HSR] {type(e).__name__}: {e}")

        jobs.append(_hsr())

    if zzz_uid:
        async def _zzz():
            try:
                output["nap"] = await fetch_zzz(client, zzz_uid)
            except Exception as e:
                print(f"[ZZZ] {type(e).__name__}: {e}")

        jobs.append(_zzz())

    if gi_uid:
        async def _gi():
            try:
                output["gi"] = await fetch_gi(client, gi_uid)
            except Exception as e:
                print(f"[GI] {type(e).__name__}: {e}")

        jobs.append(_gi())

    await asyncio.gather(*jobs)
    return output


async def main() -> None:
    cookie = os.getenv("HOYO_COOKIE", "")
    if not cookie:
        raise SystemExit("Set the HOYO_COOKIE environment variable before running.")

    hsr_raw = os.getenv("HSR_UID")
    zzz_raw = os.getenv("ZZZ_UID")
    gi_raw = os.getenv("GI_UID")

    hsr_uid = int(hsr_raw) if hsr_raw else None
    zzz_uid = int(zzz_raw) if zzz_raw else None
    gi_uid = int(gi_raw) if gi_raw else None

    if not hsr_uid and not zzz_uid and not gi_uid:
        raise SystemExit("Set at least one of HSR_UID, ZZZ_UID, or GI_UID.")

    data = await get_hoyolab_data(cookie, hsr_uid=hsr_uid, zzz_uid=zzz_uid, gi_uid=gi_uid)
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
