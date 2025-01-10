import pandas as pd
import os

def excel_to_csv(input_excel_file, output_csv_file=None):
    """
    Converts an Excel file into a CSV file.

    Parameters:
    input_excel_file (str): The path to the Excel file.
    output_csv_file (str): The path to save the CSV file. If None, saves in the same directory as the input file.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_excel_file):
            raise FileNotFoundError(f"Excel file not found at: {input_excel_file}")
        
        # Read the Excel file (first sheet by default)
        df = pd.read_excel(input_excel_file, engine="openpyxl")

        # If no output file is specified, create a default one
        if output_csv_file is None:
            output_csv_file = input_excel_file.replace(".xlsx", ".csv")

        # Save the DataFrame to a CSV file
        df.to_csv(output_csv_file, index=False)
        print(f"CSV file successfully created at: {output_csv_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_excel_file = "/Users/f.aktas/Desktop/dsa project/musteri-yolculuk.xlsx"
output_csv_file = "/Users/f.aktas/Desktop/dsa project/musteri-yolculuk.csv"  # Optional

# Convert Excel to CSV
excel_to_csv(input_excel_file, output_csv_file)