from __future__ import annotations

from rich.console import Console

from models import DownloadProgress


console = Console()


def update(
    progress: DownloadProgress,
) -> None:

    console.print(
        f"{progress.percentage:.1f}% | {progress.status.value}",
        end="\r",
    )