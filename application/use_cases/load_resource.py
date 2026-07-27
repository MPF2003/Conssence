from __future__ import annotations

from services import (
    MetadataService,
    ValidationService,
)
from workflow import DownloadWorkflow


class LoadResource:

    def __init__(
        self,
        workflow: DownloadWorkflow,
        metadata_service: MetadataService,
        validation_service: ValidationService,
    ) -> None:

        self._workflow = workflow
        self._metadata_service = metadata_service
        self._validation_service = validation_service

    def execute(
        self,
        url: str,
    ) -> None:

        if not self._validation_service.validate_url(
            url,
        ):
            raise ValueError(
                "Invalid URL.",
            )

        resource = self._metadata_service.get(
            url,
        )

        self._workflow.state.url = url
        self._workflow.state.resource = resource