from __future__ import annotations

from dataclasses import dataclass, field

from .enums import ResourceType


@dataclass(slots=True)
class ResourceInfo:
    """
    Represents a YouTube resource.
    """

    url: str

    resource_type: ResourceType

    title: str

    uploader: str | None = None

    duration: int | None = None

    video_count: int | None = None

    thumbnail: str | None = None

    description: str | None = None

    upload_date: str | None = None

    channel: str | None = None

    channel_id: str | None = None

    channel_url: str | None = None

    webpage_url: str | None = None

    extractor: str | None = None

    extractor_key: str | None = None

    view_count: int | None = None

    like_count: int | None = None

    comment_count: int | None = None

    availability: str | None = None

    language: str | None = None

    live_status: str | None = None

    age_limit: int = 0

    is_live: bool = False

    was_live: bool = False

    tags: list[str] = field(default_factory=list)

    categories: list[str] = field(default_factory=list)

    subtitles: dict = field(default_factory=dict)

    automatic_captions: dict = field(default_factory=dict)

    entries: list["ResourceInfo"] = field(default_factory=list)

    @property
    def is_video(self) -> bool:

        return self.resource_type is ResourceType.VIDEO

    @property
    def is_playlist(self) -> bool:

        return self.resource_type is ResourceType.PLAYLIST

    @property
    def has_subtitles(self) -> bool:

        return bool(
            self.subtitles
            or self.automatic_captions
        )