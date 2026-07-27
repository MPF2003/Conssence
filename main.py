from __future__ import annotations

from application import create_application
from cli.cli_app import CliApplication


def main() -> None:

    application = create_application()

    cli = CliApplication(application)

    cli.run()


if __name__ == "__main__":
    main()