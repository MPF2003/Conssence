from __future__ import annotations

from typing import Any


class Container:

    def __init__(self) -> None:

        self._services: dict[type, Any] = {}

    def register(
        self,
        service_type: type,
        instance: Any,
    ) -> None:

        self._services[service_type] = instance

    def resolve(
        self,
        service_type: type,
    ) -> Any:

        return self._services[service_type]