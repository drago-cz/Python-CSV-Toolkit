import pandas as pd
import os

def load_csv(filename):
    try:
        # Attempts to load the file with a comma delimiter
        data = pd.read_csv(filename)
        return data
    except pd.errors.ParserError:
        # If an error occurs, tries to load with a semicolon delimiter
        data = pd.read_csv(filename, delimiter=';', quotechar='"')
        return data

def list_csv_files():
    # Retrieves a list of all .csv files in the current directory
    csv_files = [file for file in os.listdir('.') if file.lower().endswith('.csv')]
    return csv_files

def main():
    # List all CSV files in the current directory
    csv_files = list_csv_files()

    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    print("Available CSV files:")
    for index, file in enumerate(csv_files, 1):
        print(f"{index}. {file}")

    # Prompt the user to select a file by number
    while True:
        try:
            selection = int(input("\nEnter the number of the CSV file you want to process: "))
            if 1 <= selection <= len(csv_files):
                filename = csv_files[selection - 1]
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Load the selected CSV file into a DataFrame
    try:
        data = load_csv(filename)
    except FileNotFoundError:
        print(f"File '{filename}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return

    # Display the column names
    print("\nColumn names in the file:")
    for index, column in enumerate(data.columns, 1):
        print(f"{index}. {column}")

    # Prompt to select a column for grouping data
    while True:
        try:
            column_choice = int(input("\nEnter the column number to group the data by: "))
            if 1 <= column_choice <= len(data.columns):
                column_name = data.columns[column_choice - 1]
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Aggregate the data
    aggregated_data = data.groupby(column_name).size().reset_index(name='Row Count')

    # Save the aggregated data to a new CSV file
    aggregated_data.to_csv("export.csv", index=False)
    print("\nAggregated data has been saved to 'export.csv'.")

if __name__ == "__main__":
    main()