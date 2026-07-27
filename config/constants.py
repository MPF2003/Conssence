from __future__ import annotations

APP_NAME = "YouTube Downloader"

APP_VERSION = "2.0.0"

DEFAULT_OUTPUT_DIR = "downloads"

DEFAULT_VIDEO_FORMAT = "bestvideo+bestaudio/best"

DEFAULT_SUBTITLE_FORMAT = "srt"

SUPPORTED_AUDIO_FORMATS = (
    "best",
    "mp3",
    "m4a",
    "flac",
    "wav",
)

SUPPORTED_VIDEO_QUALITIES = (
    "best",
    "1080p",
    "720p",
    "480p",
)

DEFAULT_SUBTITLE_LANGUAGES = (
    "en",
)

YTDLP_RETRIES = 10

SLEEP_INTERVAL = (
    1,
    5,
)