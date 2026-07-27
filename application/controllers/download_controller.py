from __future__ import annotations

from pathlib import Path

from models import (
    AudioFormat,
    ContentType,
    SubtitleMode,
)

from workflow import (
    DownloadWorkflow,
    Step,
)

from application.use_cases import (
    ConfigureDownload,
    GetSummary,
    LoadResource,
    ResetWorkflow,
    StartDownload,
)


class DownloadController:

    def __init__(
        self,
        workflow: DownloadWorkflow,
        load_resource: LoadResource,
        configure_download: ConfigureDownload,
        start_download: StartDownload,
        reset_workflow: ResetWorkflow,
        get_summary: GetSummary,
    ) -> None:

        self._workflow = workflow

        self._load_resource = load_resource
        self._configure_download = configure_download
        self._start_download = start_download
        self._reset_workflow = reset_workflow
        self._get_summary = get_summary

    # ------------------------------------------------------------------
    # Workflow
    # ------------------------------------------------------------------
    @property
    def workflow(self) -> DownloadWorkflow:
        return self._workflow

    @property
    def current_step(self) -> Step:

        return self._workflow.current_step

    @property
    def state(self):

        return self._workflow.state

    def next(
        self,
        step: Step,
    ) -> None:

        self._workflow.go_next(step)

    def back(
        self,
    ):

        return self._workflow.go_back()

    def reset(
        self,
    ) -> None:

        self._reset_workflow.execute()

    # ------------------------------------------------------------------
    # Resource
    # ------------------------------------------------------------------

    def load_resource(
        self,
        url: str,
    ) -> None:

        self._load_resource.execute(
            url,
        )

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def configure_download(
        self,
        *,
        content_type: ContentType,
        subtitle_mode: SubtitleMode,
        audio_format: AudioFormat,
        output_directory: str | Path,
    ) -> None:

        self._configure_download.execute(
            content_type=content_type,
            subtitle_mode=subtitle_mode,
            audio_format=audio_format,
            output_directory=output_directory,
        )

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(
        self,
    ) -> dict:

        return self._get_summary.execute()

    # ------------------------------------------------------------------
    # Download
    # ------------------------------------------------------------------

    def start_download(
        self,
    ):

        return self._start_download.execute()