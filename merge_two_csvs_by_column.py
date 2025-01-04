import os
import pandas as pd
import html

def list_csv_files():
    """
    Retrieves and lists all .csv files in the current directory.
    
    Returns:
        list: A list of CSV file names.
    """
    csv_files = [f for f in os.listdir('.') if f.lower().endswith('.csv')]
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {file}")
    return csv_files

def select_file(prompt, files):
    """
    Prompts the user to select a file by entering the corresponding number.
    
    Args:
        prompt (str): The input prompt to display to the user.
        files (list): A list of file names to choose from.
        
    Returns:
        str: The selected file name.
    """
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid number.")

def list_columns(file):
    """
    Lists all columns in the given CSV file.
    
    Args:
        file (str): The file name of the CSV to read.
        
    Returns:
        pandas.DataFrame: The DataFrame containing the CSV data.
    """
    df = pd.read_csv(file)
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    return df

def select_column(prompt, columns):
    """
    Prompts the user to select a column by entering the corresponding number.
    
    Args:
        prompt (str): The input prompt to display to the user.
        columns (list): A list of column names to choose from.
        
    Returns:
        str: The selected column name.
    """
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(columns):
                return columns[choice - 1]
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid number.")

def merge_files(file1, file2, column):
    """
    Merges two CSV files based on a common column.
    
    Args:
        file1 (str): The first CSV file name.
        file2 (str): The second CSV file name.
        column (str): The column name to merge on.
        
    Returns:
        pandas.DataFrame: The merged DataFrame.
    """
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Check if the selected column exists in both files
    if column not in df1.columns:
        print(f"Error: Column '{column}' does not exist in '{file1}'.")
        return None
    if column not in df2.columns:
        print(f"Error: Column '{column}' does not exist in '{file2}'.")
        return None

    # Remove duplicates in the second file
    df2_grouped = df2.groupby(column).agg(lambda x: x.iloc[0]).reset_index()

    # Decode HTML entities in the join column (only for text data)
    if df1[column].dtype == 'object':
        df1[column] = df1[column].apply(html.unescape)
    if df2_grouped[column].dtype == 'object':
        df2_grouped[column] = df2_grouped[column].apply(html.unescape)

    # Merge the files
    merged_df = pd.merge(df1, df2_grouped, on=column, how='left')

    # Decode HTML entities in all text columns
    for col in merged_df.select_dtypes(include='object').columns:
        merged_df[col] = merged_df[col].apply(lambda x: html.unescape(str(x)) if pd.notnull(x) else x)

    return merged_df

def main():
    # The main function orchestrates the CSV merging process.
    # List all CSV files in the current directory
    csv_files = list_csv_files()

    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    # Select the first CSV file
    file1_name = select_file("Select the number of the first file: ", csv_files)
    # Select the second CSV file
    file2_name = select_file("Select the number of the second file: ", csv_files)

    file1_path = os.path.join(os.getcwd(), file1_name)
    file2_path = os.path.join(os.getcwd(), file2_name)

    # List columns from the first file
    print(f"\nColumns in file '{file1_name}':")
    df1 = list_columns(file1_path)

    # Select the column to merge on
    column_choice = select_column("Select the number of the column to join the files by: ", df1.columns)

    # Merge the files
    merged_df = merge_files(file1_path, file2_path, column_choice)

    if merged_df is not None:
        output_file = os.path.join(os.getcwd(), 'merged_output.csv')
        merged_df.to_csv(output_file, index=False)
        print(f"\nFiles have been successfully merged. The result is saved in '{output_file}'.")
    else:
        print("\nMerging was unsuccessful due to missing columns.")

if __name__ == "__main__":
    main()
