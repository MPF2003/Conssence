from __future__ import annotations

from models import (
    DownloadRequest,
    SubtitleMode,
)

from services import DownloadService
from workflow import DownloadWorkflow


class StartDownload:

    def __init__(
        self,
        workflow: DownloadWorkflow,
        download_service: DownloadService,
    ) -> None:

        self._workflow = workflow
        self._download_service = download_service

    def execute(self):

        state = self._workflow.state

        request = DownloadRequest(
            resource=state.resource,
            content_type=state.content_type,
            output_directory=state.output_directory,
            playlist_items=state.playlist_items,
        )

        # -----------------------------
        # Video
        # -----------------------------

        if state.video_quality:
            request.video.quality = (
                state.video_quality
            )

        if state.video_format:
            request.video.format = (
                state.video_format
            )

        if state.video_format:

            request.video.format = (
                state.video_format
            )

        # -----------------------------
        # Audio
        # -----------------------------

        if state.audio_format:

            request.audio.format = (
                state.audio_format
            )

        # -----------------------------
        # Subtitles
        # -----------------------------

        if state.subtitle_mode:

            request.subtitles.mode = (
                state.subtitle_mode
            )

            request.subtitles.enabled = (
                state.subtitle_mode
                is not SubtitleMode.NONE
            )

        return self._download_service.download(
            request,
        )