"""Dictionary related utility functions."""
from csv import DictReader


__author__ = "730484959"

"""Some helpful utility functions for working with CSV files."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close 

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], integer: int) -> dict[str, list[str]]:
    """Produces a new table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if integer >= len(table):
        return table
    else: 
        for key in table:
            i: int = 0
            values: list[str] = []
            while i < integer:
                values.append(table[key][i])
                i += 1
            result[key] = values
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    i: int = 0 
    while i < len(column_names):
        result[column_names[i]] = table[column_names[i]]
        i += 1
    return result


def concat(table: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    result: dict[str, list[str]] = {}
    for i in table:
        result[i] = table[i]
    for i in table2:
        if i in result:
            result[i] += table2[i]
        else:
            result[i] = table2[i]
    return result


def count(list_of_values: list[str]) -> dict[str, int]:
    """Counts the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    i: int = 0 
    while i < len(list_of_values):
        if list_of_values[i] in result:
            result[list_of_values[i]] += 1
        else:
            result[list_of_values[i]] = 1
        i += 1
    return result


def less_than(col: list[str], value: int) -> list[bool]:
    """Returns a table with the values less than the input value."""
    result: list[bool] = []
    for item in col:
        result.append(int(item) < value)
    return result


def masked(col: list[str], mask: list[bool]) -> list[int]:
    result: list[int] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(int(col[i]))
    return result


def column_values_int(table: list[dict[str, str]], column: str) -> list[int]:
    """Produce a list[str] of all values in a single column."""
    result: list[int] = []
    for row in table:
        item: int = int(row[column])
        result.append(item)
    return result

