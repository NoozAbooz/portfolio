from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from core import get_hoyolab_data


app = FastAPI()


def _parse_uid(name: str) -> int | None:
    raw = os.getenv(name)
    if not raw:
        return None

    try:
        return int(raw)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=f"Invalid {name} environment variable") from exc


@app.get("/")
async def hoyolab() -> JSONResponse:
    cookie = os.getenv("HOYO_COOKIE", "")
    if not cookie:
        raise HTTPException(status_code=500, detail="Missing HOYO_COOKIE environment variable")

    hsr_uid = _parse_uid("HSR_UID")
    zzz_uid = _parse_uid("ZZZ_UID")
    if not hsr_uid and not zzz_uid:
        raise HTTPException(status_code=500, detail="Set at least one of HSR_UID or ZZZ_UID")

    data = await get_hoyolab_data(cookie, hsr_uid=hsr_uid, zzz_uid=zzz_uid)
    return JSONResponse(content=data, headers={"Cache-Control": "no-store"})
