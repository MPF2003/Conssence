from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:

    def __init__(self) -> None:

        self._subscribers: dict[
            type,
            list[Callable[[Any], None]],
        ] = defaultdict(list)

    def subscribe(
        self,
        event_type: type,
        callback: Callable[[Any], None],
    ) -> None:

        self._subscribers[
            event_type
        ].append(
            callback,
        )

    def unsubscribe(
        self,
        event_type: type,
        callback: Callable[[Any], None],
    ) -> None:

        callbacks = self._subscribers.get(
            event_type,
            [],
        )

        if callback in callbacks:

            callbacks.remove(
                callback,
            )

    def publish(
        self,
        event: Any,
    ) -> None:

        for callback in self._subscribers.get(
            type(event),
            [],
        ):

            callback(
                event,
            )

    def clear(self) -> None:

        self._subscribers.clear()