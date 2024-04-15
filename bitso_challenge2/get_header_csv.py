import os
import pandas as pd


def get_header(directory):
    # List the CSV files in the directory
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

    # Get the header and data types of each column of the file and save it to a file
    headers = []
    for file in files:
        df = pd.read_csv(file)
        header_datatypes = {}
        for col_name, col_type in df.dtypes.items():
            if col_type == 'object':
                max_length = df[col_name].str.len().max()
                dtype_str = f'varchar({max_length})'
            else:
                dtype_str = str(col_type)
            header_datatypes[col_name] = dtype_str
        headers.append({os.path.basename(file): header_datatypes})

    return headers


# Directory where the files are located
output_directory = "./outputs/"

# Get the header
master_header = get_header(output_directory)

# Build the text string for the header
header_str = ''
for header_dict in master_header:
    for file_name, dtype_dict in header_dict.items():
        header_str += f"{file_name}:\n"
        for column, dtype in dtype_dict.items():
            header_str += f"- {column}: {dtype}\n"
        header_str += "\n"

# Save the header to a file
output_file = os.path.join(output_directory, "all_sources_header.csv")
with open(output_file, 'w') as f:
    f.write(header_str)

print(f"The header for each csv file has been saved in '{output_file}'.")
