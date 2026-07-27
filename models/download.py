from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .enums import (
    AudioFormat,
    ContentType,
    SubtitleMode,
    VideoQuality,
    VideoFormat
)
from .resource import ResourceInfo


@dataclass(slots=True)
class VideoOptions:
    """
    Video download configuration.
    """

    quality: VideoQuality = VideoQuality.BEST

    format: VideoFormat = VideoFormat.AUTO

    format_selector: str = "bestvideo+bestaudio/best"

    embed_subtitles: bool = True

    embed_metadata: bool = True

    embed_thumbnail: bool = False

    write_description: bool = False

    write_info_json: bool = False


@dataclass(slots=True)
class AudioOptions:
    """
    Audio download configuration.
    """

    format: AudioFormat = AudioFormat.BEST

    bitrate: str = "320"

    embed_metadata: bool = True

    embed_thumbnail: bool = True


@dataclass(slots=True)
class SubtitleOptions:
    """
    Subtitle download configuration.
    """

    enabled: bool = False

    mode: SubtitleMode = SubtitleMode.NONE

    languages: tuple[str, ...] = ("en",)

    convert_to: str = "srt"

    embed: bool = False


@dataclass(slots=True)
class DownloadRequest:
    """
    Complete download request.
    """

    resource: ResourceInfo

    content_type: ContentType

    output_directory: Path

    playlist_items: str | None = None

    overwrite: bool = False

    retries: int = 10

    video: VideoOptions = field(
        default_factory=VideoOptions,
    )

    audio: AudioOptions = field(
        default_factory=AudioOptions,
    )

    subtitles: SubtitleOptions = field(
        default_factory=SubtitleOptions,
    )