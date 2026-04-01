from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


def _strip_wrapping_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _find_env_local() -> Path | None:
    current = Path(__file__).resolve().parent
    for directory in (current, *current.parents):
        candidate = directory / ".env.local"
        if candidate.is_file():
            return candidate
    return None


@lru_cache(maxsize=1)
def _read_env_local() -> dict[str, str]:
    env_path = _find_env_local()
    if env_path is None:
        return {}

    values: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue

        if entry.startswith("export "):
            entry = entry[7:].strip()

        if "=" not in entry:
            continue

        key, raw_value = entry.split("=", 1)
        key = key.strip()
        if not key:
            continue

        values[key] = _strip_wrapping_quotes(raw_value.strip())

    return values


def getenv_with_local_fallback(name: str, default: str | None = None) -> str | None:
    """Read environment variable, falling back to .env.local when undefined."""
    value = os.getenv(name)
    if value is not None:
        return value
    return _read_env_local().get(name, default)