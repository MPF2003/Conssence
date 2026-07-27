from __future__ import annotations

import yt_dlp

from core.option_builder import OptionBuilder
from exceptions import DownloadError
from models import DownloadRequest


class DownloadClient:
    """
    Low-level yt-dlp download client.

    Responsibilities:
        - Build yt-dlp options
        - Execute downloads
        - Nothing else
    """

    def __init__(
        self,
        option_builder: OptionBuilder,
    ) -> None:

        self._option_builder = option_builder

    def download(
        self,
        request: DownloadRequest,
        progress_hook=None,
    ) -> None:

        options = self._option_builder.build(
            request,
        )

        if progress_hook is not None:

            options.setdefault(
                "progress_hooks",
                [],
            ).append(
                progress_hook,
            )

        try:

            with yt_dlp.YoutubeDL(
                options,
            ) as ydl:

                ydl.download(
                    [
                        request.resource.url,
                    ],
                )

        except Exception as exc:

            raise DownloadError(
                str(exc),
            ) from exc

    def extract_info(
        self,
        request: DownloadRequest,
    ) -> dict:

        options = self._option_builder.build(
            request,
        )

        options["skip_download"] = True

        try:

            with yt_dlp.YoutubeDL(
                options,
            ) as ydl:

                return ydl.extract_info(
                    request.resource.url,
                    download=False,
                )

        except Exception as exc:

            raise DownloadError(
                str(exc),
            ) from exc