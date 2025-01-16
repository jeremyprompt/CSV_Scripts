import pandas as pd

def concatenate_and_remove_duplicates(csv1_path, csv2_path, output_path):
    # Load the CSV files into DataFrames
    df1 = pd.read_csv(csv1_path)
    df2 = pd.read_csv(csv2_path)

    # Concatenate the two DataFrames
    combined_df = pd.concat([df1, df2])

    # Drop duplicates, keeping only entries that appear once
    unique_df = combined_df[combined_df.duplicated(keep=False) == False]

    # Save the unique entries to a new CSV file
    unique_df.to_csv(output_path, index=False)

    print(f"Unique entries have been saved to {output_path}")

# Example usage
csv1_path = ''
csv2_path = ''
output_path = ''

concatenate_and_remove_duplicates(csv1_path, csv2_path, output_path)
