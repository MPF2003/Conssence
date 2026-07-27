from __future__ import annotations

from cli.console import console


def show() -> None:

    console.print()

    console.rule("[bold cyan]YouTube Downloader[/]")

    console.print(
        "[green]Paste a YouTube video or playlist URL to begin.[/]"
    )

    console.print()