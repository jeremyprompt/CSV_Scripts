#concatenate csv data into a master csv
import pandas as pd

# Create a list of input CSV file paths
input_files = [
    "path/to/file1.csv",
    "path/to/file2.csv",
    "path/to/file3.csv",
    # Add more files as needed
]

# Read and concatenate all CSV files
dataframes = [pd.read_csv(file) for file in input_files]
result = pd.concat(dataframes, ignore_index=True)

# Specify output file path
output_file = "path/to/output.csv"
result.to_csv(output_file, index=False)