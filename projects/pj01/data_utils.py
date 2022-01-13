"""Utility functions for Project 01."""

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


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary with the counts of unique elements in a list."""
    result_dictionary = {x: input_list.count(x) for x in input_list}

    return result_dictionary


def data_filter(values1: list[str], values2: list[str], query: str) -> dict[str, int]:
    value1_list = []
    value2_list = []

    for i in range(len(values1)): 
        value1_list.append(values1[i])
    
    for i in range(len(values2)):
        value2_list.append(values2[i])

    second_list = []
    third_list = []
    for i in range(len(value1_list)):
        if value1_list[i] == query:
            second_list.append(value1_list[i])
            third_list.append(value2_list[i])
        
    return count(third_list)


def average_rating_calculator(input_dict: dict[str, int]) -> float:
    average_list_holder = []
    total_number_of_items = []
    for i in input_dict:
        average_list_holder.append(int(i) * input_dict[i])
        total_number_of_items.append(input_dict[i])

    return sum(average_list_holder) / sum(total_number_of_items)


    