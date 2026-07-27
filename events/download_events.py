from __future__ import annotations

from dataclasses import dataclass

from models import (
    DownloadProgress,
    DownloadResult,
    ResourceInfo,
)


@dataclass(slots=True)
class MetadataLoadedEvent:
    resource: ResourceInfo


@dataclass(slots=True)
class DownloadStartedEvent:
    url: str


@dataclass(slots=True)
class DownloadProgressEvent:
    progress: DownloadProgress


@dataclass(slots=True)
class DownloadFinishedEvent:
    result: DownloadResult


@dataclass(slots=True)
class DownloadFailedEvent:
    error: str


@dataclass(slots=True)
class LogEvent:
    message: str