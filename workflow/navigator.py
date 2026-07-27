from __future__ import annotations

from enum import Enum, auto


class Step(Enum):

    URL = auto()

    METADATA = auto()

    PLAYLIST = auto()

    CONTENT = auto()

    VIDEO = auto()

    AUDIO = auto()

    SUBTITLES = auto()

    OUTPUT = auto()

    SUMMARY = auto()

    DOWNLOAD = auto()

    FINISHED = auto()


class Navigator:

    def __init__(self) -> None:

        self._history: list[Step] = []

    def next(
        self,
        step: Step,
    ) -> None:

        self._history.append(
            step,
        )

    def back(self) -> Step | None:

        if len(self._history) <= 1:

            return None

        self._history.pop()

        return self._history[-1]

    @property
    def current(
        self,
    ) -> Step | None:

        if not self._history:

            return None

        return self._history[-1]

    def reset(
        self,
    ) -> None:

        self._history.clear()