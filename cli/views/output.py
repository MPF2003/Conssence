from __future__ import annotations

from pathlib import Path


BACK = "__BACK__"


def ask() -> Path | str:

    value = input(
        "Output folder (blank=downloads, back): "
    ).strip()

    if value.lower() == "back":

        return BACK

    if not value:

        return Path.cwd()

    value = value.strip('"')
    value = value.strip("'")


    return Path(value)