import pandas as pd
import os
import re

def load_csv(filename):
    try:
        # Tries to load a CSV file where the columns are separated by a comma (,)
        data = pd.read_csv(filename)
        return data
    except pd.errors.ParserError:
        # if an error occurs, tries to load with semicolon (;) separator
        data = pd.read_csv(filename, delimiter=';', quotechar='"')
        return data

def list_csv_files():
    # Retrieves a list of all .csv files in the current directory
    csv_files = [file for file in os.listdir('.') if file.lower().endswith('.csv')]
    return csv_files

def clean_numeric(value):
    # Function for removing spaces and converting the value to float.
    if pd.isna(value):
        return None, False
    # Removes all spaces
    value_str = str(value).replace(' ', '')
    # Replaces the comma with a dot
    value_str = value_str.replace(',', '.')
    # Use regex to validate the number
    if re.match(r'^-?\d+(\.\d+)?$', value_str):
        try:
            return float(value_str), True
        except ValueError:
            return None, False
    else:
        return None, False

def main():
    # Lists all CSV files in the current directory
    csv_files = list_csv_files()

    if not csv_files:
        print("No CSV files were found in the current directory.")
        return

    print("Available CSV files:")
    for index, file in enumerate(csv_files, 1):
        print(f"{index}. {file}")

    # Allows the user to select a file by number
    while True:
        try:
            selection = int(input("\nEnter the number of the CSV file you want to process: "))
            if 1 <= selection <= len(csv_files):
                filename = csv_files[selection - 1]
                break
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Loads the selected CSV file into the DataFrame
    try:
        data = load_csv(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return

    # Displays column names
    print("\nColumn names in the file:")
    for index, column in enumerate(data.columns, 1):
        print(f"{index}. {column}")

    # Lets the user select a column for aggregation
    while True:
        try:
            group_choice = int(input("\nEnter the column number to be used for aggregation: "))
            if 1 <= group_choice <= len(data.columns):
                group_column = data.columns[group_choice - 1]
                break
            else:
                print("Invalid number. Try again")
        except ValueError:
            print("Please enter a valid number.")

    # Lets the user select a column of numeric values to be summed
    while True:
        try:
            numeric_choice = int(input("\nEnter the number of the column with the numeric values to sum them together: "))
            if 1 <= numeric_choice <= len(data.columns):
                numeric_column = data.columns[numeric_choice - 1]
                break
            else:
                print("Invalid number. Try again")
        except ValueError:
            print("Please enter a valid number.")

    # Initializing lists for valid and non-valid values
    valid_values = []
    invalid_entries = []

    # Performs numeric column cleaning and validation
    for idx, value in data[numeric_column].items():
        cleaned_value, is_valid = clean_numeric(value)
        if is_valid:
            valid_values.append(cleaned_value)
        else:
            invalid_entries.append((idx + 1, value))  # Uloží řádek a nevalidní hodnotu

    # Adds a new column with plain numeric values
    data['__cleaned_numeric'] = valid_values + [None] * (len(data) - len(valid_values))

    # Aggregates data by the selected column and sums the numeric values
    aggregated_data = data.groupby(group_column)['__cleaned_numeric'].sum().reset_index(name='Suma')

    # Saves aggregated data to a new CSV file export_suma.csv
    export_filename = "export_suma.csv"
    aggregated_data.to_csv(export_filename, index=False)
    print(f"\nThe aggregated data was saved to '{export_filename}'.")

    # Statistics of valid and non-valid values
    total_valid = len(valid_values)
    total_invalid = len(invalid_entries)

    print("\nStatistics of valid and non-valid values:")
    print(f"Valid numbers: {total_valid}")
    print(f"Numbers of invalid values: {total_invalid}")

    if total_invalid > 0:
        print("\nInvalid values:")
        for row, val in invalid_entries:
            print(f"Row {row}: {val}")

if __name__ == "__main__":
    main()
