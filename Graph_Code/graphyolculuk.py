import pandas as pd
import matplotlib.pyplot as plt

def generate_histogram_for_end_points(input_excel_file, output_graph_file):
    """
    Generates a histogram showing all ending points and their frequency.

    Parameters:
    input_excel_file (str): Path to the input Excel file.
    output_graph_file (str): Path to save the generated histogram image.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_excel_file, engine="openpyxl")

        # Ensure the required column exists
        end_column = 'Bitiş Adresi'
        if end_column not in df.columns:
            raise ValueError(f"Column '{end_column}' is missing in the data. Available columns: {df.columns.tolist()}")

        # Count the frequency of each ending point
        end_point_counts = df[end_column].value_counts()

        # Plot histogram
        plt.figure(figsize=(12, 8))
        plt.bar(end_point_counts.index, end_point_counts.values, color='#800020', edgecolor='black', alpha=0.7)
        plt.title('Histogram of Ending Points', fontsize=16)
        plt.xlabel('Ending Points', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(rotation=90, fontsize=10)
        plt.tight_layout()

        # Save and show the histogram
        plt.savefig(output_graph_file)
        plt.show()

        print(f"Histogram successfully saved to: {output_graph_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
input_excel_file = "/Users/f.aktas/Desktop/dsaproject/musteri-yolculuk.xlsx"  # Input Excel file
output_graph_file = "/Users/f.aktas/Desktop/dsaproject/end_points_histogram.png"  # Output histogram file

# Run the function
generate_histogram_for_end_points(input_excel_file, output_graph_file)
