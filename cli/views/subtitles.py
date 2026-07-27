from __future__ import annotations

from models import SubtitleMode


BACK = "__BACK__"


def ask() -> SubtitleMode | str:

    print(
        """
Subtitle options:

1. No subtitles
2. Manual subtitles
3. Automatic subtitles
4. Both manual and automatic
5. Back
"""
    )

    while True:

        choice = input(
            "Choose subtitle mode: "
        ).strip()

        match choice:

            case "1":

                return SubtitleMode.NONE

            case "2":

                return SubtitleMode.MANUAL

            case "3":

                return SubtitleMode.AUTO

            case "4":

                return SubtitleMode.BOTH

            case "5":

                return BACK

            case _:

                print(
                    "Invalid option. Try again."
                )