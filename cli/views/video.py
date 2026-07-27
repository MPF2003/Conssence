from __future__ import annotations

from dataclasses import dataclass

from models import (
    SubtitleMode,
    VideoFormat,
    VideoQuality
)


BACK = "__BACK__"


@dataclass(slots=True)
class VideoSelection:

    format: VideoFormat

    subtitles: SubtitleMode

    quality: VideoQuality

def ask() -> VideoSelection | str:

    print()

    quality = ask_quality()

    if quality == BACK:

        return BACK

    print()

    video_format = ask_format()

    if video_format == BACK:

        return BACK

    print()

    print("Subtitle mode")

    print("1. Without subtitles")

    print("2. Manual subtitles")

    print("3. Auto subtitles")

    print("4. Both")

    print("0. Back")

    while True:

        choice = input("> ").strip()

        match choice:

            case "1":

                return VideoSelection(
                    quality=quality,
                    format=video_format,
                    subtitles=SubtitleMode.NONE,
                )

            case "2":

                return VideoSelection(
                    quality=quality,
                    format=video_format,
                    subtitles=SubtitleMode.MANUAL,
                )

            case "3":

                return VideoSelection(
                    quality=quality,
                    format=video_format,
                    subtitles=SubtitleMode.AUTO,
                )

            case "4":

                return VideoSelection(
                    quality=quality,
                    format=video_format,
                    subtitles=SubtitleMode.BOTH,
                )

            case "0":

                return BACK

            case _:

                print("Invalid option.")


def ask_format() -> VideoFormat | str:

    print()

    print("Preferred format")

    print("1. Automatic (Recommended)")

    print("2. MP4")

    print("3. MKV")

    print("4. WEBM")

    print("0. Back")

    while True:

        choice = input("> ").strip()

        match choice:

            case "1":

                return VideoFormat.AUTO

            case "2":

                return VideoFormat.MP4

            case "3":

                return VideoFormat.MKV

            case "4":

                return VideoFormat.WEBM

            case "0":

                return BACK

            case _:

                print("Invalid option.")

def ask_quality() -> VideoQuality | str:

    print()

    print("Video quality")

    print("1. Best")
    print("2. 2160p")
    print("3. 1440p")
    print("4. 1080p")
    print("5. 720p")
    print("6. 480p")
    print("7. 360p")
    print("8. 240p")
    print("9. 144p")
    print("0. Back")

    while True:

        choice = input("> ").strip()

        match choice:

            case "1":
                return VideoQuality.BEST

            case "2":
                return VideoQuality.P2160

            case "3":
                return VideoQuality.P1440

            case "4":
                return VideoQuality.P1080

            case "5":
                return VideoQuality.P720

            case "6":
                return VideoQuality.P480

            case "7":
                return VideoQuality.P360

            case "8":
                return VideoQuality.P240

            case "9":
                return VideoQuality.P144

            case "0":
                return BACK

            case _:
                print("Invalid option.")