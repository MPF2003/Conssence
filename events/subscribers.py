from __future__ import annotations

from events.download_events import (
    DownloadFailedEvent,
    DownloadFinishedEvent,
    DownloadProgressEvent,
    DownloadStartedEvent,
    LogEvent,
    MetadataLoadedEvent,
)


class ConsoleSubscriber:

    def on_metadata(
        self,
        event: MetadataLoadedEvent,
    ) -> None:

        print(
            f"\nTitle: {event.resource.title}"
        )

    def on_download_started(
        self,
        event: DownloadStartedEvent,
    ) -> None:

        print(
            f"\nDownloading: {event.url}"
        )

    def on_progress(
        self,
        event: DownloadProgressEvent,
    ) -> None:

        print(
            f"\r{event.progress.percentage:.1f}%",
            end="",
        )

    def on_finished(
        self,
        event: DownloadFinishedEvent,
    ) -> None:

        print(
            "\nDownload completed."
        )

    def on_failed(
        self,
        event: DownloadFailedEvent,
    ) -> None:

        print(
            f"\nError: {event.error}"
        )

    def on_log(
        self,
        event: LogEvent,
    ) -> None:

        print(
            event.message,
        )