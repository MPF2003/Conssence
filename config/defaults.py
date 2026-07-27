from __future__ import annotations

from pathlib import Path

from .constants import (
    DEFAULT_OUTPUT_DIR,
    DEFAULT_SUBTITLE_FORMAT,
    DEFAULT_SUBTITLE_LANGUAGES,
    DEFAULT_VIDEO_FORMAT,
    SLEEP_INTERVAL,
    YTDLP_RETRIES,
)

DEFAULT_SETTINGS = {
    "browser": "firefox",
    "remote_components": [],
    "extractor_args": {},
    "output_directory": Path(DEFAULT_OUTPUT_DIR),
    "video_format": DEFAULT_VIDEO_FORMAT,
    "subtitle_languages": DEFAULT_SUBTITLE_LANGUAGES,
    "subtitle_format": DEFAULT_SUBTITLE_FORMAT,
    "retries": YTDLP_RETRIES,
    "sleep_interval": SLEEP_INTERVAL,
}