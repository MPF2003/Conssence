from __future__ import annotations

from application.application import Application
from application.controllers import DownloadController
from application.registry import (
    build_container,
)


def create_application() -> Application:

    container = build_container()

    controller = container.resolve(
        DownloadController,
    )

    return Application(
        controller,
    )