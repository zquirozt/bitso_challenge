from datetime import datetime
import pandas as pd
import os
import re


def iso_to_datetime(iso_date):
    # Use regex to extract the datetime part of the string
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{2})', iso_date)
    if match:
        datetime_part = match.group(1)
        # Convert to datetime object
        return datetime.strptime(datetime_part, '%Y-%m-%d %H:%M:%S.%f')
    else:
        # Handle the case when no match is found (return None or raise an exception)
        return None  # or raise ValueError("Invalid ISO date format")


def load_csv_df(path_files):
    # Load CSV files into DataFrames
    dataframes = {}
    for file in os.listdir(path_files):
        if file.endswith(".csv"):
            df_name = file.split('.')[0]
            df = pd.read_csv(os.path.join(path_files, file), header=0)

            if df_name == "event_sample_data":
                df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])
            elif df_name == "withdrawals_sample_data":
                df['event_timestamp'] = pd.to_datetime(df['event_timestamp'].apply(iso_to_datetime))
            elif df_name == "deposit_sample_data":
                df['event_timestamp'] = pd.to_datetime(df['event_timestamp'].apply(iso_to_datetime))

            # Print the data types of each field in the DataFrame
            # print(f"Data types for DataFrame '{df_name}':")
            # print(df.dtypes)
            # print()

            # Store the dataframe in the dictionary
            dataframes[df_name] = df
    return dataframes
