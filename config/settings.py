from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .defaults import DEFAULT_SETTINGS


@dataclass(slots=True)
class AppSettings:

    browser: str = DEFAULT_SETTINGS["browser"]

    remote_components: tuple[str, ...] = field(
        default_factory=tuple,
    )

    extractor_args: dict = field(
        default_factory=dict,
    )

    output_directory: Path = DEFAULT_SETTINGS[
        "output_directory"
    ]

    video_format: str = DEFAULT_SETTINGS[
        "video_format"
    ]

    subtitle_languages: tuple[str, ...] = DEFAULT_SETTINGS[
        "subtitle_languages"
    ]

    subtitle_format: str = DEFAULT_SETTINGS[
        "subtitle_format"
    ]

    retries: int = DEFAULT_SETTINGS[
        "retries"
    ]

    sleep_interval: tuple[int, int] = DEFAULT_SETTINGS[
        "sleep_interval"
    ]