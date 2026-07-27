from __future__ import annotations

from typing import Callable

from core.download_client import DownloadClient
from models import (
    DownloadProgress,
    DownloadRequest,
    DownloadResult,
    DownloadStatus,
)


class DownloadManager:
    """
    High-level download coordinator.

    Responsibilities:
        - Execute downloads
        - Track download state
        - Convert yt-dlp progress to DownloadProgress
        - Notify listeners
    """

    def __init__(
        self,
        client: DownloadClient,
    ) -> None:

        self._client = client

        self._listeners: list[
            Callable[[DownloadProgress], None]
        ] = []

    def add_listener(
        self,
        listener: Callable[
            [DownloadProgress],
            None,
        ],
    ) -> None:

        self._listeners.append(
            listener,
        )

    def remove_listener(
        self,
        listener: Callable[
            [DownloadProgress],
            None,
        ],
    ) -> None:

        if listener in self._listeners:

            self._listeners.remove(
                listener,
            )

    def download(
        self,
        request: DownloadRequest,
    ) -> DownloadResult:

        progress = DownloadProgress(
            status=DownloadStatus.PREPARING,
        )

        self._notify(
            progress,
        )

        try:

            self._client.download(
                request=request,
                progress_hook=self._progress_hook,
            )

            progress.status = (
                DownloadStatus.FINISHED
            )

            self._notify(
                progress,
            )

            return DownloadResult(
                success=True,
                status=DownloadStatus.FINISHED,
                resource_url=request.resource.url,
            )

        except Exception as exc:

            progress.status = (
                DownloadStatus.FAILED
            )

            self._notify(
                progress,
            )

            return DownloadResult(
                success=False,
                status=DownloadStatus.FAILED,
                resource_url=request.resource.url,
                error=str(exc),
            )

    def _progress_hook(
        self,
        data: dict,
    ) -> None:

        status = data.get(
            "status",
        )

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
                speed=data.get(
                    "speed",
                ),
                eta=data.get(
                    "eta",
                ),
            )

            self._notify(
                progress,
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

            self._notify(
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
            )
            or 0
        )

        if total <= 0:

            return 0.0

        return round(
            downloaded * 100 / total,
            2,
        )

    def _notify(
        self,
        progress: DownloadProgress,
    ) -> None:

        for listener in self._listeners:

            listener(
                progress,
            )