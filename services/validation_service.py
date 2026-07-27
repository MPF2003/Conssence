from __future__ import annotations

from urllib.parse import urlparse


class ValidationService:

    @staticmethod
    def validate_url(
        url: str,
    ) -> bool:

        try:

            parsed = urlparse(
                url,
            )

            return (
                parsed.scheme in (
                    "http",
                    "https",
                )
                and bool(
                    parsed.netloc,
                )
            )

        except Exception:

            return False