from __future__ import annotations

from config import AppSettings

from core import (
    DownloadClient,
    DownloadManager,
    MetadataClient,
    OptionBuilder,
)

from services import (
    DownloadService,
    MetadataService,
    PathService,
    ValidationService,
)

from workflow import DownloadWorkflow


class Providers:

    @staticmethod
    def settings() -> AppSettings:
        return AppSettings()

    @staticmethod
    def workflow() -> DownloadWorkflow:
        return DownloadWorkflow()

    @staticmethod
    def option_builder(
        settings: AppSettings,
    ) -> OptionBuilder:

        return OptionBuilder(
            settings,
        )

    @staticmethod
    def metadata_client(
        settings: AppSettings,
    ) -> MetadataClient:

        return MetadataClient(
            settings,
        )

    @staticmethod
    def download_client(
        option_builder: OptionBuilder,
    ) -> DownloadClient:

        return DownloadClient(
            option_builder,
        )

    @staticmethod
    def download_manager(
        download_client: DownloadClient,
    ) -> DownloadManager:

        return DownloadManager(
            download_client,
        )

    @staticmethod
    def metadata_service(
        metadata_client: MetadataClient,
    ) -> MetadataService:

        return MetadataService(
            metadata_client,
        )

    @staticmethod
    def download_service(
        download_manager: DownloadManager,
    ) -> DownloadService:

        return DownloadService(
            download_manager,
        )

    @staticmethod
    def validation_service() -> ValidationService:

        return ValidationService()

    @staticmethod
    def path_service() -> PathService:

        return PathService()