from __future__ import annotations

from services import SummaryService
from workflow import DownloadWorkflow


class GetSummary:

    def __init__(
        self,
        workflow: DownloadWorkflow,
    ) -> None:

        self._workflow = workflow

    def execute(self) -> dict:

        state = self._workflow.state

        summary = SummaryService.metadata(
            state.resource,
        )

        summary.update(
            {
                "content_type": (
                    state.content_type.name
                    if state.content_type
                    else None
                ),

                "audio_format": (
                    state.audio_format.value
                    if state.audio_format
                    else None
                ),

                "subtitle_mode": (
                    state.subtitle_mode.name
                    if state.subtitle_mode
                    else None
                ),

                "output_directory": (
                    str(state.output_directory)
                    if state.output_directory
                    else None
                ),

                "playlist_items": (
                    state.playlist_items
                ),
            }
        )

        return summary