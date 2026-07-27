from __future__ import annotations

from models import AudioFormat


BACK = "__BACK__"


def ask() -> AudioFormat | str:

    print()

    print("1. Best")

    print("2. MP3")

    print("3. M4A")

    print("4. FLAC")

    print("5. WAV")

    print("0. Back")

    while True:

        choice = input("> ").strip()

        match choice:

            case "1":
                return AudioFormat.BEST

            case "2":
                return AudioFormat.MP3

            case "3":
                return AudioFormat.M4A

            case "4":
                return AudioFormat.FLAC

            case "5":
                return AudioFormat.WAV

            case "0":
                return BACK

            case _:
                print("Invalid option.")