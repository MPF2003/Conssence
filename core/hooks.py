from __future__ import annotations

from collections.abc import Callable

from models import (
    DownloadProgress,
    DownloadStatus,
)


class ProgressHook:
    """
    Converts yt-dlp hook data into DownloadProgress objects.
    """

    def __init__(
        self,
        callback: Callable[[DownloadProgress], None],
    ) -> None:

        self._callback = callback

    def __call__(
        self,
        data: dict,
    ) -> None:

        status = data.get("status")

        if status == "downloading":

            progress = DownloadProgress(
                status=DownloadStatus.DOWNLOADING,
                filename=data.get(
                    "filename",
                    "",
                ),
                downloaded_bytes=data.get(
                    "downloaded_bytes",
                    0,
                ),
                total_bytes=(
                    data.get("total_bytes")
                    or data.get(
                        "total_bytes_estimate",
                        0,
                    )
                ),
                percentage=self._percentage(
                    data,
                ),
                speed=data.get("speed"),
                eta=data.get("eta"),
            )

        elif status == "finished":

            progress = DownloadProgress(
                status=DownloadStatus.POST_PROCESSING,
                filename=data.get(
                    "filename",
                    "",
                ),
                percentage=100.0,
            )

        else:

            return

        self._callback(
            progress,
        )

    @staticmethod
    def _percentage(
        data: dict,
    ) -> float:

        downloaded = data.get(
            "downloaded_bytes",
            0,
        )

        total = (
            data.get("total_bytes")
            or data.get(
                "total_bytes_estimate",
                0,
            )
        )

        if total <= 0:

            return 0.0

        return round(
            downloaded * 100 / total,
            2,
        )