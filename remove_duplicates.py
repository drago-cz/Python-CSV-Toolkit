import os
import pandas as pd

# Step 1: Display all CSV files in the current directory and create a list
def list_csv_files(directory="."):
    # Displays all CSV files in the specified directory.
    csv_files = [file for file in os.listdir(directory) if file.lower().endswith(".csv")]
    for idx, file in enumerate(csv_files):
        print(f"{idx + 1}: {file}")
    return csv_files

# Step 2: Select a CSV file from the list
def select_csv_file(csv_files):
    # Allows the user to select a CSV file from the list.
    try:
        choice = int(input("Enter the number of the file you want to open: ")) - 1
        if 0 <= choice < len(csv_files):
            return csv_files[choice]
        else:
            print("Invalid choice. Please try again.")
            return select_csv_file(csv_files)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_csv_file(csv_files)

# Step 3: Load the file with support for multiple delimiters
def load_csv_with_varied_delimiters(file_path):
    # Loads a CSV file with support for multiple delimiters (comma and semicolon).
    delimiters = [',', ';']
    for delimiter in delimiters:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter)
            print(f"File loaded with delimiter '{delimiter}'")
            return df
        except pd.errors.ParserError:
            continue
    raise ValueError("Failed to load the file with supported delimiters.")

# Step 4: Display the list of columns and select a column
def select_column(df):
    # Displays column names and allows the user to select one.
    print("Available columns:")
    for idx, column in enumerate(df.columns):
        print(f"{idx + 1}: {column}")
    try:
        choice = int(input("Enter the number of the column to remove duplicates by: ")) - 1
        if 0 <= choice < len(df.columns):
            return df.columns[choice]
        else:
            print("Invalid choice. Please try again.")
            return select_column(df)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_column(df)

# Step 5: Remove duplicates based on the selected column and display statistics
def remove_duplicates_and_show_stats(df, column_name):
    # Removes duplicate rows based on the selected column and displays statistics.
    initial_row_count = len(df)
    df = df.drop_duplicates(subset=column_name)
    final_row_count = len(df)
    removed_count = initial_row_count - final_row_count

    print(f"\nStatistics:")
    print(f"Number of rows before removing duplicates: {initial_row_count}")
    print(f"Number of rows after removing duplicates: {final_row_count}")
    print(f"Number of duplicate rows removed: {removed_count}")

    return df

# Main part of the script
def main():
    # 1. Display all CSV files
    print("List of CSV files in the directory:")
    csv_files = list_csv_files()

    if not csv_files:
        print("There are no CSV files in the directory.")
        return

    # 2. Select a specific file
    selected_file = select_csv_file(csv_files)
    print(f"\nOpened file: {selected_file}")

    # 3. Load the file with support for multiple delimiters
    try:
        df = load_csv_with_varied_delimiters(selected_file)
    except ValueError as e:
        print(e)
        return

    # 4. Display the list of columns and select a column
    selected_column = select_column(df)
    print(f"\nSelected column for removing duplicates: {selected_column}")

    # 5. Remove duplicates and display statistics
    df = remove_duplicates_and_show_stats(df, selected_column)

    # 6. Save the cleaned DataFrame to a new file
    output_file = f"cleaned_{selected_file}"
    df.to_csv(output_file, index=False)
    print(f"\nThe cleaned file has been saved as '{output_file}'")

if __name__ == "__main__":
    main()
