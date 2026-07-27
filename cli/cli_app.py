from __future__ import annotations
from application import Application
from workflow import Step

from .folder_picker import choose_folder

from .views import (
    audio,
    content,
    home,
    playlist,
    subtitles,
    summary,
    url,
    video,
    edit,
    output
)


class CliApplication:

    def __init__(
        self,
        application: Application,
    ) -> None:

        self.app = application
        self.download = application.download

    def run(self) -> None:

        home.show()

        while True:

            try:

                result = self._run_step()

                if result == "exit":
                    break

            except Exception as error:

                print(
                    f"\nError: {error}"
                )

                input(
                    "\nPress Enter to continue..."
                )

    def _run_step(self):

        workflow = self.download.workflow

        match workflow.current_step:

            case Step.URL:

                result = url.ask()

                if result == url.BACK:
                    return

                self.download.load_resource(
                    result,
                )

                workflow.go_next(
                    Step.METADATA,
                )


            case Step.METADATA:

                if workflow.state.resource.is_playlist:

                    workflow.go_next(
                        Step.PLAYLIST,
                    )

                else:

                    workflow.go_next(
                        Step.CONTENT,
                    )


            case Step.PLAYLIST:

                result = playlist.ask(
                    workflow.state.resource.video_count,
                )

                if result == playlist.BACK:

                    workflow.go_back()

                    return

                workflow.state.playlist_items = result

                workflow.go_next(
                    Step.CONTENT,
                )


            case Step.CONTENT:

                result = content.ask()

                if result == content.BACK:

                    workflow.go_back()

                    return

                workflow.state.content_type = result

                if result.name == "VIDEO":

                    workflow.go_next(
                        Step.VIDEO,
                    )

                elif result.name == "AUDIO":

                    workflow.go_next(
                        Step.AUDIO,
                    )

                else:

                    workflow.go_next(
                        Step.SUBTITLES,
                    )

            case Step.VIDEO:

                result = video.ask()

                if result == video.BACK:
                    workflow.go_back()

                    return

                workflow.state.video_quality = (
                    result.quality
                )

                workflow.state.video_format = (
                    result.format
                )

                workflow.state.subtitle_mode = (
                    result.subtitles
                )

                workflow.go_next(
                    Step.OUTPUT,
                )


            case Step.AUDIO:

                result = audio.ask()

                if result == audio.BACK:

                    workflow.go_back()

                    return

                workflow.state.audio_format = result

                workflow.go_next(
                    Step.OUTPUT,
                )

            case Step.SUBTITLES:

                result = subtitles.ask()

                if result == subtitles.BACK:
                    workflow.go_back()

                    return

                workflow.state.subtitle_mode = result

                workflow.go_next(
                    Step.OUTPUT,
                )


            case Step.OUTPUT:

                print(
                    "\nPlease select output folder..."
                )

                result = choose_folder()

                if result is None:

                    print(
                        "\nNo folder selected."
                    )

                    return

                self.download.configure_download(
                    content_type=workflow.state.content_type,
                    subtitle_mode=workflow.state.subtitle_mode,
                    audio_format=workflow.state.audio_format,
                    output_directory=result,
                )

                workflow.go_next(
                    Step.SUMMARY,
                )

            case Step.SUMMARY:

                summary.show(
                    workflow.state,
                )

                action = summary.ask_action()

                if action == "1":

                    workflow.go_next(
                        Step.DOWNLOAD,
                    )

                elif action == "2":

                    result = edit.ask(
                        workflow.state,
                    )

                    if result != edit.BACK:
                        self._handle_edit(
                            result,
                        )

                elif action == "3":

                    return "exit"

                elif action == "2":

                    workflow.go_back()

                else:

                    return "exit"


            case Step.DOWNLOAD:

                result = self.download.start_download()

                print()

                if result.success:

                    print(
                        "Download completed."
                    )

                else:

                    print(
                        f"Download failed: {result.error}"
                    )

                workflow.go_next(
                    Step.FINISHED,
                )


            case Step.FINISHED:

                answer = input(
                    "\nDownload another? (y/n): "
                ).strip().lower()

                if answer == "y":

                    self.download.reset()

                    home.show()

                else:

                    return "exit"

        return None

    def _handle_edit(
            self,
            option: str,
    ) -> None:

        workflow = self.download.workflow

        match option:

            # -----------------------------
            # Video
            # -----------------------------

            case "video":

                result = video.ask()

                if result != video.BACK:
                    workflow.state.video_format = (
                        result.format
                    )

                    workflow.state.subtitle_mode = (
                        result.subtitles
                    )

            # -----------------------------
            # Audio
            # -----------------------------

            case "audio":

                result = audio.ask()

                if result != audio.BACK:
                    workflow.state.audio_format = result

            # -----------------------------
            # Subtitle
            # -----------------------------

            case "subtitles":

                result = subtitles.ask()

                if result != subtitles.BACK:
                    workflow.state.subtitle_mode = result

            # -----------------------------
            # Playlist
            # -----------------------------

            case "playlist":

                result = playlist.ask(
                    workflow.state.resource.video_count,
                )

                if result != playlist.BACK:
                    workflow.state.playlist_items = result

            # -----------------------------
            # Output
            # -----------------------------

            case "output":

                result = output.ask()

                if result != output.BACK:
                    self.download.configure_download(
                        content_type=workflow.state.content_type,
                        subtitle_mode=workflow.state.subtitle_mode,
                        audio_format=workflow.state.audio_format,
                        output_directory=result,
                    )