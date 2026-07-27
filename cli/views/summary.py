from __future__ import annotations

from rich import print

from workflow import DownloadState


def show(
    state: DownloadState,
) -> None:

    print()

    print("[bold]Summary[/]")

    print(
        f"URL        : {state.url}"
    )

    print(
        f"Content    : {state.content_type}"
    )

    print(
        f"Output     : {state.output_directory}"
    )

    if state.resource.is_playlist:

        if state.playlist_items:

            print(
                f"Playlist   : {state.playlist_items}"
            )

        else:

            print(
                "Playlist   : All items"
            )

    if state.audio_format:

        print(
            f"Audio      : {state.audio_format}"
        )

    if state.subtitle_mode:

        print(
            f"Subtitles  : {state.subtitle_mode}"
        )

    print()


def ask_action() -> str:

    print(
        """
[bold]What do you want to do?[/]

1. Start download
2. Edit settings
3. Cancel
"""
    )

    return input(
        "Choose: "
    ).strip()