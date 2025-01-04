# Test version 1.0
import os
import pandas as pd

# Step 1: Display all CSV files in the current directory and create a list
def list_csv_files(directory="."):
    # Lists all CSV files in the specified directory.
    csv_files = [file for file in os.listdir(directory) if file.lower().endswith(".csv")]
    for idx, file in enumerate(csv_files):
        print(f"{idx + 1}: {file}")  # Prints each CSV file with a number.
    return csv_files  # Returns the list of CSV files.

# Step 2: Select a CSV file from the list
def select_csv_file(csv_files):
    # Allows the user to select a CSV file from the list.
    try:
        choice = int(input("Enter the number of the file you want to open: ")) - 1  # Prompts user for file number.
        if 0 <= choice < len(csv_files):
            return csv_files[choice]  # Returns the selected file.
        else:
            print("Invalid choice. Please try again.")  # Notifies user of invalid choice.
            return select_csv_file(csv_files)  # Recursively prompts again.
    except ValueError:
        print("Invalid input. Please enter a number.")  # Notifies user of invalid input.
        return select_csv_file(csv_files)  # Recursively prompts again.

# Step 3: Load the file with support for multiple delimiters
def load_csv_with_varied_delimiters(file_path):
    # Loads a CSV file with support for multiple delimiters (comma and semicolon).
    delimiters = [',', ';']  # List of possible delimiters.
    for delimiter in delimiters:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter, dtype=str)  # Reads CSV with current delimiter.
            print(f"File loaded with delimiter '{delimiter}'")  # Notifies which delimiter was used.
            return df  # Returns the loaded DataFrame.
        except pd.errors.ParserError:
            continue  # Tries the next delimiter if parsing fails.
    raise ValueError("Failed to load the file with supported delimiters.")  # Raises error if all delimiters fail.

# Step 4: Scan the dataset for missing or null values
def scan_missing_values(df):
    report = {}  # Initializes a dictionary to store summary of issues.
    detailed_issues = {}  # Initializes a dictionary to store detailed issues.
    for column in df.columns:
        missing_count = df[column].isna().sum()  # Counts missing (NaN) values in the column.
        empty_after_strip = df[column].astype(str).str.strip().eq('').sum()  # Counts empty values after stripping whitespace.
        
        total_issues = missing_count + empty_after_strip  # Calculates total issues in the column.
        if total_issues > 0:
            report[column] = {
                'missing': missing_count,  # Stores count of missing values.
                'empty_after_strip': empty_after_strip,  # Stores count of empty values after stripping.
                'total': total_issues  # Stores total count of issues.
            }
            
            # Identifies rows with issues.
            issues = []
            for idx, value in df[column].items():  # Changed iteritems() to items()
                if pd.isna(value):
                    issues.append((idx + 2, 'Missing value'))  # Appends row number and issue type for missing values.
                elif isinstance(value, str) and value.strip() == '':
                    issues.append((idx + 2, 'Empty value after stripping'))  # Appends row number and issue type for empty values.
            detailed_issues[column] = issues  # Stores detailed issues for the column.
    return report, detailed_issues  # Returns the summary and detailed issues.

# Step 5: Generate and save the detailed report
def generate_report(report, detailed_issues, report_filename="detailed_report.txt"):
    with open(report_filename, 'w', encoding='utf-8') as file:
        for column, issues in detailed_issues.items():
            file.write(f"Column: {column}\n")  # Writes the column name.
            for row_num, issue in issues:
                file.write(f"  Row {row_num}: {issue}\n")  # Writes each issue with row number and description.
            file.write("\n")  # Adds a newline for separation between columns.
    print(f"Detailed report saved to '{report_filename}'.")  # Notifies user of report creation.

# Main part of the script
def main():
    # 1. Display all CSV files.
    print("List of CSV files in the directory:")
    csv_files = list_csv_files()  # Retrieves and prints CSV files.

    if not csv_files:
        print("There are no CSV files in the directory.")  # Notifies if no CSV files are found.
        return  # Exits the script.

    # 2. Select a specific file.
    selected_file = select_csv_file(csv_files)  # Prompts user to select a file.
    print(f"\nOpened file: {selected_file}")  # Notifies which file was opened.

    # 3. Load the file with support for multiple delimiters.
    try:
        df = load_csv_with_varied_delimiters(selected_file)  # Attempts to load the selected CSV file.
    except ValueError as e:
        print(e)  # Prints error message if loading fails.
        return  # Exits the script.

    # 4. Scan the dataset for missing or null values.
    report, detailed_issues = scan_missing_values(df)  # Scans for missing and empty values.

    if not report:
        print("Everything is okay. No missing or empty values were found.")  # Notifies if no issues are found.
    else:
        print("Issues were found in the data:")  # Notifies that issues were found.
        for column, counts in report.items():
            print(f"Column '{column}':")  # Prints the column name.
            print(f"  Missing values: {counts['missing']}")  # Prints count of missing values.
            print(f"  Empty values after stripping: {counts['empty_after_strip']}")  # Prints count of empty values after stripping.
            print(f"  Total issues: {counts['total']}\n")  # Prints total count of issues.

        # 5. Generate and save the detailed report.
        generate_report(report, detailed_issues)  # Creates and saves the detailed report.

if __name__ == "__main__":
    main()  # Executes the main function when the script is run.