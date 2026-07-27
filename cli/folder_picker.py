from __future__ import annotations

from pathlib import Path
from tkinter import Tk, filedialog


def choose_folder() -> Path | None:

    root = Tk()

    root.withdraw()
    root.attributes(
        "-topmost",
        True,
    )

    folder = filedialog.askdirectory(
        title="Select output folder",
    )

    root.destroy()

    if not folder:
        return None

    return Path(folder)