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

## Acknowledgements

- Built with [Pandas](https://pandas.pydata.org/).
- Inspired by common data processing needs.