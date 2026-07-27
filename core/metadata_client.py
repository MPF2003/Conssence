from __future__ import annotations

import yt_dlp

from config import AppSettings
from exceptions import MetadataError
from models import (
    ResourceInfo,
    ResourceType,
)


class MetadataClient:
    """
    Responsible for extracting metadata from YouTube resources.
    """

    def __init__(
        self,
        settings: AppSettings,
    ) -> None:

        self._settings = settings

    def extract(
        self,
        url: str,
    ) -> ResourceInfo:

        options = {
            "quiet": True,
            "skip_download": True,
            "extract_flat": False,
            "cookiesfrombrowser": (
                self._settings.browser,
            ),
            "remote_components": list(
                self._settings.remote_components,
            ),
            "extractor_args": (
                self._settings.extractor_args
            ),
        }

        try:

            with yt_dlp.YoutubeDL(
                options,
            ) as ydl:

                info = ydl.extract_info(
                    url,
                    download=False,
                )

        except Exception as exc:

            raise MetadataError(
                str(exc),
            ) from exc

        return self._build_resource(
            url,
            info,
        )

    def _build_resource(
        self,
        url: str,
        info: dict,
    ) -> ResourceInfo:

        resource_type = (
            ResourceType.PLAYLIST
            if info.get("entries")
            else ResourceType.VIDEO
        )

        return ResourceInfo(
            url=url,
            resource_type=resource_type,
            title=info.get("title", ""),
            uploader=info.get("uploader"),
            duration=info.get("duration"),
            video_count=(
                len(info["entries"])
                if info.get("entries")
                else None
            ),
            thumbnail=info.get("thumbnail"),
            description=info.get("description"),
            upload_date=info.get("upload_date"),
            channel=info.get("channel"),
            channel_id=info.get("channel_id"),
            channel_url=info.get("channel_url"),
            webpage_url=info.get("webpage_url"),
            extractor=info.get("extractor"),
            extractor_key=info.get("extractor_key"),
            view_count=info.get("view_count"),
            like_count=info.get("like_count"),
            comment_count=info.get("comment_count"),
            availability=info.get("availability"),
            language=info.get("language"),
            live_status=info.get("live_status"),
            age_limit=info.get("age_limit", 0),
            is_live=info.get("is_live", False),
            was_live=info.get("was_live", False),
            tags=info.get("tags", []),
            categories=info.get("categories", []),
            subtitles=info.get("subtitles", {}),
            automatic_captions=info.get(
                "automatic_captions",
                {},
            ),
        )