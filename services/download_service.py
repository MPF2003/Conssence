from __future__ import annotations

from core.download_manager import DownloadManager
from models import (
    DownloadRequest,
    DownloadResult,
)


class DownloadService:
    """
    Application layer for downloads.
    """

    def __init__(
        self,
        manager: DownloadManager,
    ) -> None:

        self._manager = manager

    def download(
        self,
        request: DownloadRequest,
    ) -> DownloadResult:

        return self._manager.download(
            request,
        )