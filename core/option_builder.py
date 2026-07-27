from __future__ import annotations

from pathlib import Path

from config import AppSettings
from models import (
    ContentType,
    DownloadRequest,
    SubtitleMode,
    VideoFormat
)


class OptionBuilder:
    """
    Builds yt-dlp options from a DownloadRequest.
    """

    def __init__(
        self,
        settings: AppSettings,
    ) -> None:

        self._settings = settings

    def build(
        self,
        request: DownloadRequest,
    ) -> dict:

        output_directory = Path(
            request.output_directory,
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        options = {
            "quiet": False,
            "noprogress": False,
            "overwrites": request.overwrite,
            "retries": request.retries,

            "paths": {
                "home": str(
                    output_directory,
                ),
            },

            "outtmpl": (
                "%(title)s.%(ext)s"
            ),

            "windowsfilenames": True,
            "ignoreerrors": False,
            "continuedl": True,

            "sleep_interval": (
                self._settings.sleep_interval[0]
            ),

            "max_sleep_interval": (
                self._settings.sleep_interval[1]
            ),

            "cookiesfrombrowser": (
                self._settings.browser,
            ),

            "remote_components": list(
                self._settings.remote_components,
            ),

            "extractor_args": (
                self._settings.extractor_args
            ),

            "playlist_items": (
                request.playlist_items
            ),
        }

        match request.content_type:

            case ContentType.VIDEO:

                self._configure_video(
                    options,
                    request,
                )

            case ContentType.AUDIO:

                self._configure_audio(
                    options,
                    request,
                )

            case ContentType.SUBTITLES:

                self._configure_subtitles(
                    options,
                    request,
                )

        return options

    def _configure_video(
            self,
            options: dict,
            request: DownloadRequest,
    ) -> None:

        options["format"] = (
            self._build_video_format(
                request,
            )
        )

        # -----------------------------------
        # Preferred output format
        # -----------------------------------

        if (
                request.video.format
                is not VideoFormat.AUTO
        ):
            options["merge_output_format"] = (
                request.video.format.value
            )

        options["embedmetadata"] = (
            request.video.embed_metadata
        )

        options["embedthumbnail"] = (
            request.video.embed_thumbnail
        )

        options["writedescription"] = (
            request.video.write_description
        )

        options["writeinfojson"] = (
            request.video.write_info_json
        )

        if request.subtitles.enabled:
            self._apply_subtitles(
                options,
                request,
            )

            options["embedsubtitles"] = (
                request.video.embed_subtitles
            )

    def _configure_audio(
            self,
            options: dict,
            request: DownloadRequest,
    ) -> None:

        options["format"] = "bestaudio/best"

        options["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": request.audio.format.value,
                "preferredquality": request.audio.bitrate,
            },
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
            },
        ]

        options["embedmetadata"] = (
            request.audio.embed_metadata
        )

        options["writethumbnail"] = True

        options["embedthumbnail"] = (
            request.audio.embed_thumbnail
        )

        options["parse_metadata"] = [
            "%(uploader)s:%(artist)s",
        ]

    def _configure_subtitles(
        self,
        options: dict,
        request: DownloadRequest,
    ) -> None:

        options["skip_download"] = True

        self._apply_subtitles(
            options,
            request,
        )

    def _apply_subtitles(
        self,
        options: dict,
        request: DownloadRequest,
    ) -> None:

        options["writesubtitles"] = (
            request.subtitles.mode
            in (
                SubtitleMode.MANUAL,
                SubtitleMode.BOTH,
            )
        )

        options["writeautomaticsub"] = (
            request.subtitles.mode
            in (
                SubtitleMode.AUTO,
                SubtitleMode.BOTH,
            )
        )

        options["subtitleslangs"] = list(
            request.subtitles.languages
        )

        options["subtitlesformat"] = (
            request.subtitles.convert_to
        )

    def _build_video_format(
            self,
            request: DownloadRequest,
    ) -> str:

        quality = request.video.quality

        if quality.value == "best":
            return (
                "bv*+ba/b"
            )

        height = quality.value.removesuffix(
            "p",
        )

        return (
            f"bestvideo[height<={height}]+bestaudio/"
            f"best[height<={height}]"
        )