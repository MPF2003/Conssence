from __future__ import annotations

from models import ContentType


BACK = "__BACK__"


def ask() -> ContentType | str:

    print()

    print("1. Video")

    print("2. Audio")

    print("3. Subtitles")

    print("0. Back")

    while True:

        choice = input("> ").strip()

        match choice:

            case "1":
                return ContentType.VIDEO

            case "2":
                return ContentType.AUDIO

            case "3":
                return ContentType.SUBTITLES

            case "0":
                return BACK

            case _:
                print("Invalid option.")