from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .enums import DownloadStatus


@dataclass(slots=True)
class DownloadProgress:
    """
    Current download progress.
    """

    status: DownloadStatus = DownloadStatus.PENDING

    filename: str = ""

    downloaded_bytes: int = 0

    total_bytes: int = 0

    percentage: float = 0.0

    speed: float | None = None

    eta: int | None = None

    playlist_index: int | None = None

    playlist_count: int | None = None


@dataclass(slots=True)
class DownloadResult:
    """
    Final download result.
    """

    success: bool

    status: DownloadStatus

    resource_url: str

    output_path: Path | None = None

    elapsed_time: float = 0.0

    downloaded_files: list[Path] | None = None

    error: str | None = None