from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core import get_hoyolab_data
from env_utils import getenv_with_local_fallback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)


def _parse_uid(name: str) -> int | None:
    raw = getenv_with_local_fallback(name)
    if not raw:
        return None

    try:
        return int(raw)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=f"Invalid {name} environment variable") from exc


@app.get("/")
async def hoyolab() -> JSONResponse:
    cookie = getenv_with_local_fallback("HOYO_COOKIE", "")
    if not cookie:
        raise HTTPException(status_code=500, detail="Missing HOYO_COOKIE environment variable")

    hsr_uid = _parse_uid("HSR_UID")
    zzz_uid = _parse_uid("ZZZ_UID")
    gi_uid = _parse_uid("GI_UID")
    if not hsr_uid and not zzz_uid and not gi_uid:
        raise HTTPException(
            status_code=500,
            detail="Set at least one of HSR_UID, ZZZ_UID, or GI_UID",
        )

    data = await get_hoyolab_data(
        cookie,
        hsr_uid=hsr_uid,
        zzz_uid=zzz_uid,
        gi_uid=gi_uid,
    )
    return JSONResponse(content=data, headers={"Cache-Control": "no-store"})
