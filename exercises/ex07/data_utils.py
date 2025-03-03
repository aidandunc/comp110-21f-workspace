"""Utility functions."""

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
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], numberN: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first numberN rows of data of each column."""
    first_rows: dict[str, list[str]] = {}

    if numberN <= len(table):
        bound = numberN
    else: 
        bound = len(table)
    for i in table:
        column_list: list[str] = []
        table_list = table[i]
        if numberN == 0:
            first_rows[i] = []
        else:
            j = 0
            while j < bound:
                column_list.append(table_list[j])
                first_rows[i] = column_list
                j += 1

    return first_rows


def select(input_dictionary: dict[str, list[str]], column_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns.""" 
    final_list: dict[str, list[str]] = {}

    for i in input_dictionary:
        if i in column_list:
            final_list[i] = input_dictionary[i]

    return final_list


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    final_concatenated_list: dict[str, list[str]] = {}

    for i in table1:
        final_concatenated_list[i] = table1[i]

    shared_keys = []
    table2_specific = []

    for j in table2:
        if j in final_concatenated_list.keys():
            shared_keys.append(j)
        else:
            table2_specific.append(j)
        
    for count in shared_keys:
        final_concatenated_list[count] += table2[count]
    for counter in table2_specific:
        final_concatenated_list[counter] = table2[counter]

    return final_concatenated_list


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary with the counts of unique elements in a list."""
    result_dictionary = {x: input_list.count(x) for x in input_list}

    return result_dictionary