import pandas as pd

def remove_duplicates(master_file, sub_file, id_column='ID'):
    """
    Remove rows from master CSV file if their IDs exist in sub CSV file
    
    Args:
        master_file (str): Path to master CSV file
        sub_file (str): Path to sub CSV file
        id_column (str): Name of the ID column to match (default: 'ID')
    
    Returns:
        DataFrame: Master data with duplicates removed
    """
    # Read the CSV files
    master_df = pd.read_csv(master_file)
    sub_df = pd.read_csv(sub_file)
    
    # Get list of IDs from sub file
    sub_ids = sub_df[id_column].unique()
    
    # Remove rows from master where ID is in sub_ids
    filtered_master = master_df[~master_df[id_column].isin(sub_ids)]
    
    return filtered_master

def main():
    # File paths
    master_file = ''
    sub_file = ''
    
    # Remove duplicates
    result = remove_duplicates(master_file, sub_file)
    
    # Save result to new CSV file
    output_file = ''
    result.to_csv(output_file, index=False)
    print(f"Filtered master list saved to {output_file}")

if __name__ == "__main__":
    main()
