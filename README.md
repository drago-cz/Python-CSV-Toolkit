# Python CSV Toolkit

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

**Python CSV Toolkit** is a set of Python scripts aimed at simplifying and automating common CSV data manipulation tasks. Whether you're a beginner learning Python or a data enthusiast looking for handy tools, this toolkit offers functionalities to help you efficiently manage your CSV data.

## Features

- **Remove Duplicates (`remove_duplicates.py`):**
  - Identify and remove duplicate rows based on a selected column.
  - Provides statistics on the number of duplicates removed.

- **Merge CSV Files (`merge_two_csvs_by_column.py`):**
  - Merge two CSV files based on a common column.
  - Handles HTML entity decoding and duplicate removal in the merging process.

- **Aggregate Data (`aggregate_csv_by_column.py`):**
  - Group data by a specified column and aggregate row counts.
  - Supports different delimiters for loading CSV files.

- **Find Missing Values (`find_missing_values.py`):**
  - Scan a CSV file for missing, null, or empty values.
  - Provides a summary report of issues found.
  - Generates a detailed text report with specific locations of the issues.

- **Aggregate and Sum CSV (`aggregate_and_sum_csv.py`):**
  - Groups data by a selected column and sums numeric values after cleaning them.
  - Cleans numeric data by removing spaces and converting values to floats.
  - Provides statistics on valid and invalid numeric entries.
  - Saves the aggregated data to a new CSV file.

## Getting Started

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

- **Required Python Libraries:**
  - `pandas`

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/drago-cz/Python-CSV-Toolkit.git
   ```

2. **Install Dependencies:**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pandas
   ```  

## Usage

Each script is designed to be run from the command line. Below are instructions for each script.

### 1. Remove Duplicates

**Script:** `remove_duplicates.py`

**Description:** Removes duplicate rows from a CSV file based on a selected column.

**Run the Script:**

```bash
python remove_duplicates.py
```

**Steps:**

1. The script will list all CSV files in the current directory.
2. Select the CSV file you want to process by entering its corresponding number.
3. Choose the column based on which duplicates will be removed by entering its corresponding number.
4. The cleaned CSV will be saved as `cleaned_<original_filename>.csv`.

### 2. Merge Two CSVs by Column

**Script:** `merge_two_csvs_by_column.py`

**Description:** Merges two CSV files based on a common column.

**Run the Script:**

```bash
python merge_two_csvs_by_column.py
```

**Steps:**

1. The script will list all CSV files in the current directory.
2. Select the first and second CSV files to merge by entering their corresponding numbers.
3. Choose the column to merge the files on by entering its corresponding number.
4. The merged CSV will be saved as `merged_output.csv`.

### 3. Aggregate CSV by Column

**Script:** `aggregate_csv_by_column.py`

**Description:** Aggregates data in a CSV file by grouping rows based on a selected column and counts the number of occurrences.

**Run the Script:**

```bash
python aggregate_csv_by_column.py
```

**Steps:**

1. The script will list all CSV files in the current directory.
2. Select the CSV file you want to aggregate by entering its corresponding number.
3. Choose the column to group the data by by entering its corresponding number.
4. The aggregated data will be saved as `export.csv`.

### 4. Find Missing Values

**Script:** `find_missing_values.py`

**Description:** Scans a CSV file for missing, null, or empty values and generates a detailed report.

**Run the Script:**

```bash
python find_missing_values.py
```

**Steps:**

1. The script will list all CSV files in the current directory.
2. Select the CSV file you want to scan by entering its corresponding number.
3. The script will analyze the selected CSV for missing or empty values.
   - If no issues are found, it will notify you that everything is okay.
   - If issues are detected, it will display a summary of the problems.
4. If issues are found, a detailed report will be saved as `detailed_report.txt`, listing each problematic column along with the specific rows and types of issues.

**Example Output:**

```
List of CSV files in the directory:
1: data1.csv
2: data2.csv
Enter the number of the file you want to open: 1

Opened file: data1.csv
File loaded with delimiter ','
Issues were found in the data:
Column 'Name':
  Missing values: 2
  Empty values after stripping: 1
  Total issues: 3

Column 'Email':
  Missing values: 0
  Empty values after stripping: 2
  Total issues: 2

Detailed report saved to 'detailed_report.txt'.
```

**Content of `detailed_report.txt`:**

```
Column: Name
  Row 3: Missing value
  Row 5: Empty value after stripping
  Row 8: Missing value

Column: Email
  Row 2: Empty value after stripping
  Row 6: Empty value after stripping
```

### 5. Aggregate and Sum CSV

**Script:** `aggregate_and_sum_csv.py`

**Description:** Groups data by a specified column and sums numeric values after cleaning the data.

**Run the Script:**

```bash
python aggregate_and_sum_csv.py
```

**Steps:**

1. The script will list all CSV files in the current directory.
2. Select the CSV file you want to process by entering its corresponding number.
3. Choose the column to group the data by by entering its corresponding number.
4. Choose the column containing numeric values to sum by entering its corresponding number.
5. The script will clean the numeric data by removing spaces, replacing commas with dots, and validating the numbers.
6. It will aggregate the data based on the selected grouping column and sum the cleaned numeric values.
7. The aggregated data will be saved as `export_suma.csv`.
8. The script will display statistics of valid and invalid values and list invalid entries if any.

**Example Output:**

```
List of CSV files in the directory:
1: sales_data.csv
2: inventory.csv
Enter the number of the CSV file you want to process: 1

Available CSV files:
1. sales_data.csv
2. inventory.csv
Enter the number of the CSV file you want to process: 1

Column names in the file:
1. Product
2. Quantity Sold
3. Revenue

Enter the column number to be used for aggregation: 1
Enter the number of the column with the numeric values to sum them together: 3

The aggregated data was saved to 'export_suma.csv'.

Statistics of valid and non-valid values:
Valid numbers: 150
Numbers of invalid values: 3

Invalid values:
Row 10: "N/A"
Row 25: "unknown"
Row 47: " - "
```

## Acknowledgements

- Built with [Pandas](https://pandas.pydata.org/).
- Inspired by common data processing needs.
- Special thanks to ChatGPT (o1-mini) for helping identify errors, suggesting improvements, and enhancing code comments.