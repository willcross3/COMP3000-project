import csv
from pathlib import Path

# Allow unusually large timeline fields, such as long event messages.
csv.field_size_limit(2**31 - 1)


def read_timeline(path: Path) -> list[Event]:
    """Read Plaso timeline events from a CSV file after validating the header."""
    with path.open(mode="r", encoding="utf-8", newline="") as handle:
        # Use the CSV parser so quoted commas and embedded line breaks are handled correctly.
        reader = csv.reader(handle)

        # Validate the schema before processing any event rows.
        header = next(reader, None)
        if header is None or tuple(header) != EXPECTED_COLUMNS:
            raise HeaderMismatchError(
                f"Header mismatch in '{path}': expected {EXPECTED_COLUMNS}, got {header}"
            )

        events: list[Event] = []
        for row_number, row in enumerate(reader, start=1):
            # Reject malformed rows instead of assigning values to the wrong fields.
            if len(row) != len(EXPECTED_COLUMNS):
                raise ValueError(
                    f"{path} (row {row_number}): expected {len(EXPECTED_COLUMNS)} columns, "
                    f"got {len(row)}"
                )

            dt, timestamp_desc, source, source_long, message, parser, display_name, tag = row
            # Convert each CSV row into the application's event representation.
            events.append(
                Event(
                    timeline=path.stem,
                    row_id=row_number,
                    datetime=dt,
                    timestamp_desc=timestamp_desc,
                    source=source,
                    source_long=source_long,
                    message=message,
                    parser=parser,
                    file=display_name,
                    tag=tag,
                    raw=tuple(row),
                )
            )

    return events