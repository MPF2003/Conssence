from __future__ import annotations

from application.container import Container
from application.controllers import DownloadController
from application.providers import Providers

from application.use_cases import (
    ConfigureDownload,
    GetSummary,
    LoadResource,
    ResetWorkflow,
    StartDownload,
)


def build_container() -> Container:

    container = Container()

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    settings = Providers.settings()

    # ------------------------------------------------------------------
    # Workflow
    # ------------------------------------------------------------------

    workflow = Providers.workflow()

    # ------------------------------------------------------------------
    # Core
    # ------------------------------------------------------------------

    option_builder = Providers.option_builder(
        settings,
    )

    metadata_client = Providers.metadata_client(
        settings,
    )

    download_client = Providers.download_client(
        option_builder,
    )

    download_manager = Providers.download_manager(
        download_client,
    )

    # ------------------------------------------------------------------
    # Services
    # ------------------------------------------------------------------

    metadata_service = Providers.metadata_service(
        metadata_client,
    )

    download_service = Providers.download_service(
        download_manager,
    )

    validation_service = (
        Providers.validation_service()
    )

    path_service = (
        Providers.path_service()
    )

    # ------------------------------------------------------------------
    # Use Cases
    # ------------------------------------------------------------------

    load_resource = LoadResource(
        workflow=workflow,
        metadata_service=metadata_service,
        validation_service=validation_service,
    )

    configure_download = ConfigureDownload(
        workflow=workflow,
        path_service=path_service,
    )

    start_download = StartDownload(
        workflow=workflow,
        download_service=download_service,
    )

    reset_workflow = ResetWorkflow(
        workflow=workflow,
    )

    get_summary = GetSummary(
        workflow=workflow,
    )

    # ------------------------------------------------------------------
    # Controller
    # ------------------------------------------------------------------

    controller = DownloadController(
        workflow=workflow,
        load_resource=load_resource,
        configure_download=configure_download,
        start_download=start_download,
        reset_workflow=reset_workflow,
        get_summary=get_summary,
    )

    # ------------------------------------------------------------------
    # Container
    # ------------------------------------------------------------------

    container.register(
        DownloadController,
        controller,
    )

    return container