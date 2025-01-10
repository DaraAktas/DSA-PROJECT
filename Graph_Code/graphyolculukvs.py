import pandas as pd
import matplotlib.pyplot as plt

def plot_location_vs_all(input_excel_file, output_graph_file, filter_location):
    """
    Generates a graph comparing points that start or end with a specific location vs all data.

    Parameters:
    input_excel_file (str): Path to the input Excel file.
    output_graph_file (str): Path to save the generated graph image.
    filter_location (str): The location to filter for.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_excel_file, engine="openpyxl")

        # Ensure the required columns exist
        required_columns = ['Başlangıç Adresi', 'Bitiş Adresi']
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' is missing in the data. Available columns: {df.columns.tolist()}")

        # Total number of rows in the dataset
        total_points = len(df)

        # Filter rows where the start or end location matches the specified location
        filtered_df = df[(df['Başlangıç Adresi'] == filter_location) | (df['Bitiş Adresi'] == filter_location)]
        location_points = len(filtered_df)

        if total_points == 0:
            raise ValueError("The dataset is empty. No data to analyze.")

        # Prepare data for plotting
        categories = ['Points at Location', 'All Data']
        counts = [location_points, total_points]

        # Plot the graph
        plt.figure(figsize=(8, 6))
        plt.bar(categories, counts, color=['#800020', 'gray'])
        plt.title(f'Points Starting/Ending at "{filter_location}" vs All Data')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.xticks(rotation=15)
        plt.tight_layout()

        # Save and show the graph
        plt.savefig(output_graph_file)
        plt.show()

        print(f"Graph successfully saved to: {output_graph_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths and parameters
input_excel_file = "/Users/f.aktas/Desktop/dsaproject/musteri-yolculuk.xlsx"  # Input Excel file
output_graph_file = "/Users/f.aktas/Desktop/dsaproject/location_vs_all_graph.png"  # Output graph file
filter_location = "Orta Mah., Cengizhan Cad., Tuzla"  # Location to filter for

# Run the function
plot_location_vs_all(input_excel_file, output_graph_file, filter_location)