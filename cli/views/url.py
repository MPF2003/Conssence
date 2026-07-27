from __future__ import annotations

from cli.console import console


BACK = "__BACK__"


def ask() -> str:

    while True:

        value = input(
            "URL (or 'back'): "
        ).strip()

        if value:

            if value.lower() == "back":

                return BACK

            return value

        console.print(
            "[red]URL cannot be empty.[/]"
        )