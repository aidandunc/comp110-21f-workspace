"""Some helpful utility functions for working with CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # close file when done to free its resoruces
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""

    result: list[str] = []

    for row in table:
        item: list[str] = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result