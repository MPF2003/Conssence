from __future__ import annotations

from services import EditCapabilityService


BACK = "__BACK__"


_LABELS = {
    "video": "Video settings",
    "audio": "Audio settings",
    "subtitles": "Subtitle settings",
    "playlist": "Playlist range",
    "output": "Output folder",
}


def ask(state) -> str:

    capabilities = EditCapabilityService.available(
        state,
    )

    print()
    print("Edit Settings")
    print()

    mapping: dict[str, str] = {}

    index = 1

    for capability in capabilities:

        print(
            f"{index}. {_LABELS[capability]}"
        )

        mapping[str(index)] = capability

        index += 1

    print(
        f"{index}. Back"
    )

    mapping[str(index)] = BACK

    while True:

        choice = input(
            "\nChoose option: "
        ).strip()

        if choice in mapping:

            return mapping[choice]

        print(
            "Invalid option."
        )