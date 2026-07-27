from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from models import (
    AudioFormat,
    ContentType,
    ResourceInfo,
    SubtitleMode,
    VideoQuality,
    VideoFormat
)



@dataclass(slots=True)
class DownloadState:
    """
    Shared state of the download workflow.
    """

    url: str = ""

    resource: ResourceInfo | None = None

    content_type: ContentType | None = None

    video_quality: VideoQuality = VideoQuality.BEST

    subtitle_mode: SubtitleMode = SubtitleMode.NONE

    audio_format: AudioFormat = AudioFormat.BEST

    output_directory: Path | None = None

    video_format: VideoFormat = VideoFormat.AUTO

    playlist_items: str | None = None

    overwrite: bool = False