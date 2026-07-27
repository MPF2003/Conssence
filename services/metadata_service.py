from __future__ import annotations

from core.metadata_client import MetadataClient
from models import ResourceInfo


class MetadataService:
    """
    Application layer for metadata extraction.
    """

    def __init__(
        self,
        client: MetadataClient,
    ) -> None:

        self._client = client

    def get(
        self,
        url: str,
    ) -> ResourceInfo:

        return self._client.extract(
            url,
        )