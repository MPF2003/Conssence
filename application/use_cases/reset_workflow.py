from __future__ import annotations

from workflow import DownloadWorkflow


class ResetWorkflow:

    def __init__(
        self,
        workflow: DownloadWorkflow,
    ) -> None:

        self._workflow = workflow

    def execute(self) -> None:

        self._workflow.reset()