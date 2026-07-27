from pathlib import Path

from core.utils import ensure_directory


class PathService:

    def resolve(
        self,
        directory: str | Path,
    ) -> Path:

        print(
            "PATH SERVICE FILE:",
            __file__,
        )

        print(
            "BEFORE:",
            repr(directory),
            type(directory),
        )

        directory = str(directory)

        directory = directory.strip()

        directory = directory.strip('"')
        directory = directory.strip("'")

        print(
            "AFTER:",
            repr(directory),
        )

        path = Path(directory)

        print(
            "FINAL PATH:",
            repr(path),
        )

        return ensure_directory(
            path,
        )