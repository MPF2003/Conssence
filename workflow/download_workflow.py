from __future__ import annotations

from workflow.download_state import DownloadState
from workflow.navigator import (
    Navigator,
    Step,
)


class DownloadWorkflow:

    def __init__(self) -> None:

        self.state = DownloadState()

        self.navigator = Navigator()

        self.navigator.next(
            Step.URL,
        )

    @property
    def current_step(
        self,
    ) -> Step:

        return self.navigator.current

    def go_next(
        self,
        step: Step,
    ) -> None:

        self.navigator.next(
            step,
        )

    def go_back(
        self,
    ) -> Step | None:

        return self.navigator.back()

    def reset(
        self,
    ) -> None:

        self.state = DownloadState()

        self.navigator.reset()

        self.navigator.next(
            Step.URL,
        )