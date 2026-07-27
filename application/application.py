from __future__ import annotations

from application.controllers import DownloadController


class Application:

    def __init__(
        self,
        download_controller: DownloadController,
    ) -> None:

        self.download = download_controller