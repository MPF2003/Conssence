from __future__ import annotations

from enum import StrEnum



class ResourceType(StrEnum):
    VIDEO = "video"
    PLAYLIST = "playlist"


class ContentType(StrEnum):
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLES = "subtitles"


class SubtitleMode(StrEnum):
    NONE = "none"
    MANUAL = "manual"
    AUTO = "auto"
    BOTH = "both"


class VideoQuality(StrEnum):

    BEST = "best"

    P4320 = "4320p"

    P2160 = "2160p"

    P1440 = "1440p"

    P1080 = "1080p"

    P720 = "720p"

    P480 = "480p"

    P360 = "360p"

    P240 = "240p"

    P144 = "144p"

class VideoFormat(StrEnum):

    AUTO = "auto"

    MP4 = "mp4"

    MKV = "mkv"

    WEBM = "webm"

class AudioFormat(StrEnum):
    BEST = "best"
    MP3 = "mp3"
    M4A = "m4a"
    FLAC = "flac"
    WAV = "wav"


class DownloadStatus(StrEnum):
    PENDING = "pending"
    PREPARING = "preparing"
    DOWNLOADING = "downloading"
    POST_PROCESSING = "post_processing"
    FINISHED = "finished"
    FAILED = "failed"
    CANCELLED = "cancelled"


class EventType(StrEnum):
    DOWNLOAD_STARTED = "download_started"
    DOWNLOAD_PROGRESS = "download_progress"
    DOWNLOAD_FINISHED = "download_finished"
    DOWNLOAD_FAILED = "download_failed"

    METADATA_LOADED = "metadata_loaded"

    LOG = "log"