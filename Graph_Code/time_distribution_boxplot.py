import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

def convert_time_to_hour(original_time):
    """
    Converts a time range (e.g., "8:40 am-9:30 am") to the start hour in 24-hour format as an integer (e.g., 8).
    """
    try:
        start_time = original_time.split("-")[0]
        start_hour = int(datetime.strptime(start_time.strip(), "%I:%M %p").strftime("%H"))
        return start_hour
    except Exception as e:
        print(f"Time conversion error for '{original_time}': {e}")
        return None

def plot_time_distribution_boxplot(class_schedule_file, taxi_usage_file, output_graph_file):
    """
    Generates a boxplot showing the distribution of class and taxi usage times for each day.
    """
    try:
        # Read the JSON schedule file and fix time formats
        with open(class_schedule_file, "r") as f:
            class_schedule = json.load(f)

        schedule_data = []
        for day, classes in class_schedule.items():
            for class_detail in classes:
                hour = convert_time_to_hour(class_detail["time"])
                if hour is not None:
                    schedule_data.append({
                        "Day": day,
                        "Hour": hour,
                        "Type": "Class"
                    })

        class_schedule_df = pd.DataFrame(schedule_data)

        # Read the taxi usage Excel file
        taxi_usage_df = pd.read_excel(taxi_usage_file, engine="openpyxl")
        taxi_usage_df['Hour'] = pd.to_datetime(taxi_usage_df['Başlangıç Zamanı'], format='%d/%m/%Y %H:%M').dt.hour
        taxi_usage_df['Day'] = pd.to_datetime(taxi_usage_df['Başlangıç Zamanı'], format='%d/%m/%Y %H:%M').dt.day_name()
        taxi_usage_df['Type'] = 'Taxi'

        # Combine both datasets
        combined_df = pd.concat([class_schedule_df, taxi_usage_df[['Day', 'Hour', 'Type']]], ignore_index=True)

        # Normalize day order for boxplot
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        combined_df['Day'] = pd.Categorical(combined_df['Day'], categories=day_order, ordered=True)

        # Plot the boxplot
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=combined_df, x='Day', y='Hour', hue='Type', order=day_order)
        plt.title('Distribution of Class and Taxi Usage Times by Day', fontsize=16)
        plt.xlabel('Day of Week', fontsize=12)
        plt.ylabel('Time of Day (Hour)', fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.legend(title='Type', loc='upper right')
        plt.tight_layout()

        # Save and show the boxplot
        plt.savefig(output_graph_file)
        plt.show()

        print(f"Boxplot successfully saved to: {output_graph_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# File paths
class_schedule_file = "/Users/f.aktas/Desktop/dsaproject/academicschedule.json"  # JSON file for class schedule
taxi_usage_file = "/Users/f.aktas/Desktop/dsaproject/musteri-yolculuk.xlsx"  # Excel file for taxi usage
output_graph_file = "/Users/f.aktas/Desktop/dsaproject/time_distribution_boxplot.png"  # Output boxplot file

# Run the function
plot_time_distribution_boxplot(class_schedule_file, taxi_usage_file, output_graph_file)