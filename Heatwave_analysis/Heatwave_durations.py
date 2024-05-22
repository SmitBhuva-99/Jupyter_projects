import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Heatwave_anomaly.csv')
districts = df.columns.tolist()
districts.remove('Date')

# Convert the 'Date' column to datetime format with the correct format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Define a function to check if five consecutive days have values greater than 0.8
def check_consecutive_5_days_above_threshold(column_values):
    consecutive_count = 0
    for value in column_values:
        if value > 0.8:
            consecutive_count += 1
            if consecutive_count == 5:  # Fixed the comparison operator
                return True
        else:
            consecutive_count = 0
    return False

for column_name in districts:
    events_count_per_year = {}  # Dictionary to store event counts for each year
    for year, group in df.groupby(df['Date'].dt.year):
        events_count = 0
        for col_values in group[column_name].rolling(window=5):  # Changed window size to 5
            if check_consecutive_5_days_above_threshold(col_values.dropna()):
                events_count += 1
        events_count_per_year[year] = events_count
    print(f"Yearly event counts for {column_name}: {events_count_per_year}")
