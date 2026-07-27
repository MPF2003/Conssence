from __future__ import annotations


BACK = "__BACK__"


def ask(
    max_items: int | None = None,
) -> str | None:

    print(
        """
Playlist options:

1. Download entire playlist
2. Download range
3. Select specific items
4. Back
"""
    )

    while True:

        choice = input(
            "Choose option: "
        ).strip()

        if choice == "4":

            return BACK

        if choice == "1":

            return None

        if choice == "2":

            while True:

                start = input(
                    "Start item: "
                ).strip()

                end = input(
                    "End item: "
                ).strip()

                try:

                    start_number = int(start)
                    end_number = int(end)

                except ValueError:

                    print(
                        "ERROR: Enter numbers only."
                    )

                    continue


                if start_number <= 0 or end_number <= 0:

                    print(
                        "ERROR: Numbers must be greater than zero."
                    )

                    continue


                if start_number > end_number:

                    print(
                        "ERROR: Start item cannot be greater than end item."
                    )

                    continue


                if (
                    max_items
                    and end_number > max_items
                ):

                    print(
                        f"ERROR: Playlist contains only {max_items} items."
                    )

                    continue


                return f"{start_number}-{end_number}"


        if choice == "3":

            while True:

                items = input(
                    "Items (example: 1,3,5): "
                ).strip()

                try:

                    numbers = [
                        int(item.strip())
                        for item in items.split(",")
                    ]

                except ValueError:

                    print(
                        "ERROR: Invalid item list."
                    )

                    continue


                if any(
                    number <= 0
                    for number in numbers
                ):

                    print(
                        "ERROR: Numbers must be greater than zero."
                    )

                    continue


                if (
                    max_items
                    and max(numbers) > max_items
                ):

                    print(
                        f"ERROR: Playlist contains only {max_items} items."
                    )

                    continue

                return ",".join(
                    str(number)
                    for number in numbers
                )


        print(
            "ERROR: Invalid option."
        )