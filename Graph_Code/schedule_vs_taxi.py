import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

def convert_time_to_hour(original_time):
    """
    Converts a time range (e.g., "8:40 am-9:30 am") to the start hour in 24-hour format (e.g., "08:00").
    """
    try:
        start_time = original_time.split("-")[0]
        start_hour = datetime.strptime(start_time.strip(), "%I:%M %p").strftime("%H:00")
        return start_hour
    except Exception as e:
        print(f"Time conversion error for '{original_time}': {e}")
        return None

def plot_time_correlation(class_schedule_file, taxi_usage_file, output_graph_file):
    """
    Generates a heatmap showing the correlation between class schedule and taxi usage times.
    """
    try:
        # Read the JSON schedule file and fix time formats
        with open(class_schedule_file, "r") as f:
            class_schedule = json.load(f)

        schedule_data = []
        for day, classes in class_schedule.items():
            for class_detail in classes:
                hour = convert_time_to_hour(class_detail["time"])
                if hour:
                    schedule_data.append({
                        "Day": day,
                        "Hour": hour,
                        "Type": "Class"
                    })

        class_schedule_df = pd.DataFrame(schedule_data)

        # Read the taxi usage Excel file
        taxi_usage_df = pd.read_excel(taxi_usage_file, engine="openpyxl")
        taxi_usage_df['Hour'] = pd.to_datetime(taxi_usage_df['Başlangıç Zamanı'], format='%d/%m/%Y %H:%M').dt.strftime('%H:00')
        taxi_usage_df['Day'] = pd.to_datetime(taxi_usage_df['Başlangıç Zamanı'], format='%d/%m/%Y %H:%M').dt.day_name()
        taxi_usage_df['Type'] = 'Taxi'

        # Combine both datasets
        combined_df = pd.concat([class_schedule_df, taxi_usage_df[['Day', 'Hour', 'Type']]], ignore_index=True)

        # Count occurrences of each combination
        heatmap_data = combined_df.pivot_table(index='Day', columns='Hour', values='Type', aggfunc='count', fill_value=0)

        # Normalize day order
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        heatmap_data = heatmap_data.reindex(day_order)

        # Plot the heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt="d", cbar_kws={'label': 'Number of Events'})
        plt.title('Time Correlation Between Class Schedule and Taxi Usage', fontsize=16)
        plt.xlabel('Hour of Day', fontsize=12)
        plt.ylabel('Day of Week', fontsize=12)
        plt.tight_layout()

        # Save and show the heatmap
        plt.savefig(output_graph_file)
        plt.show()

        print(f"Heatmap successfully saved to: {output_graph_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
class_schedule_file = "/Users/f.aktas/Desktop/dsaproject/academicschedule.json"  # JSON file for class schedule
taxi_usage_file = "/Users/f.aktas/Desktop/dsaproject/musteri-yolculuk.xlsx"  # Excel file for taxi usage
output_graph_file = "/Users/f.aktas/Desktop/dsaproject/time_correlation_heatmap.png"  # Output heatmap file

# Run the function
plot_time_correlation(class_schedule_file, taxi_usage_file, output_graph_file)