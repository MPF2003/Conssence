from __future__ import annotations

from pathlib import Path
import re


_INVALID_FILENAME = re.compile(
    r'[<>:"/\\|?*\x00-\x1F]'
)


def sanitize_filename(
    name: str,
) -> str:

    filename = _INVALID_FILENAME.sub(
        "_",
        name,
    ).strip()

    return filename.rstrip(".")


def ensure_directory(
    path: Path,
) -> Path:

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


def bytes_to_mb(
    value: int,
) -> float:

    return round(
        value / (1024 * 1024),
        2,
    )


def bytes_to_gb(
    value: int,
) -> float:

    return round(
        value / (1024 * 1024 * 1024),
        2,
    )


def format_speed(
    speed: float | None,
) -> str:

    if speed is None:

        return "--"

    return f"{bytes_to_mb(int(speed))} MB/s"


def format_eta(
    seconds: int | None,
) -> str:

    if seconds is None:

        return "--"

    minutes, sec = divmod(
        seconds,
        60,
    )

    hours, minutes = divmod(
        minutes,
        60,
    )

    if hours:

        return f"{hours:02}:{minutes:02}:{sec:02}"

    return f"{minutes:02}:{sec:02}"