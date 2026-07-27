from __future__ import annotations

from models import (
    ContentType,
    SubtitleMode,
)


class EditCapabilityService:

    @staticmethod
    def available(
        state,
    ) -> list[str]:

        options = []

        # Content specific settings

        if state.content_type is ContentType.VIDEO:

            options.append(
                "video"
            )

        elif state.content_type is ContentType.AUDIO:

            options.append(
                "audio"
            )


        # Subtitle settings

        if (
            state.content_type is ContentType.VIDEO
            and state.subtitle_mode
            is not SubtitleMode.NONE
        ):

            options.append(
                "subtitles"
            )


        # Playlist only

        if (
            state.resource
            and state.resource.is_playlist
        ):

            options.append(
                "playlist"
            )


        # Always available

        options.append(
            "output"
        )


        return options