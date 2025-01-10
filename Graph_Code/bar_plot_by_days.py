import pandas as pd
import matplotlib.pyplot as plt

def generate_bar_plot_by_days(input_excel_file, output_graph_file, date_column):
    """
    Generates a bar plot showing counts grouped by days, ordered from Monday to Sunday,
    with bars colored burgundy.

    Parameters:
    input_excel_file (str): Path to the input Excel file.
    output_graph_file (str): Path to save the generated bar plot image.
    date_column (str): The column containing date information.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_excel_file, engine="openpyxl")

        # Ensure the date column exists
        if date_column not in df.columns:
            raise ValueError(f"Column '{date_column}' is missing in the data. Available columns: {df.columns.tolist()}")

        # Convert the date column to datetime format
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

        # Drop rows with invalid dates
        df = df.dropna(subset=[date_column])

        # Extract the day of the week
        df['Day of Week'] = df[date_column].dt.day_name()

        # Define the correct order of days
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Count occurrences by day and reorder
        day_counts = df['Day of Week'].value_counts().reindex(day_order, fill_value=0)

        # Plot the bar graph with burgundy bars
        plt.figure(figsize=(10, 6))
        plt.bar(day_counts.index, day_counts.values, color='#800020', edgecolor='black')  # Burgundy color
        plt.title('Record Counts by Days of the Week', fontsize=16)
        plt.xlabel('Days of the Week', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()

        # Save and show the bar plot
        plt.savefig(output_graph_file)
        plt.show()

        print(f"Bar plot successfully saved to: {output_graph_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths and parameters
input_excel_file = "/Users/f.aktas/Desktop/dsaproject/musteri-yolculuk.xlsx"  # Input Excel file
output_graph_file = "/Users/f.aktas/Desktop/dsaproject/count_by_days_bar_plot.png"  # Output bar plot file
date_column = "Başlangıç Zamanı"  # Replace with the actual column name containing date information

# Run the function
generate_bar_plot_by_days(input_excel_file, output_graph_file, date_column)