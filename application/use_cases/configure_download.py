from __future__ import annotations

from pathlib import Path

from models import (
    AudioFormat,
    ContentType,
    SubtitleMode,
)
from services import PathService
from workflow import DownloadWorkflow


class ConfigureDownload:

    def __init__(
        self,
        workflow: DownloadWorkflow,
        path_service: PathService,
    ) -> None:

        self._workflow = workflow
        self._path_service = path_service

    def execute(
        self,
        *,
        content_type: ContentType,
        subtitle_mode: SubtitleMode,
        audio_format: AudioFormat,
        output_directory: str | Path,
    ) -> None:

        state = self._workflow.state

        state.content_type = content_type
        state.subtitle_mode = subtitle_mode
        state.audio_format = audio_format
        state.output_directory = (
            self._path_service.resolve(
                output_directory,
            )
        )