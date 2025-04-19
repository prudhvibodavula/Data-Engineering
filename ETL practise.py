import pandas as pd
def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_csv(file_name)

# Extracting data from the raw_data.csv file
extracted_data = extract(file_name="raw_data.csv")
# Transform the extracted_data
transformed_data = transform(data_frame = extracted_data)
# Load the transformed data into a cleaned_data.csv
load(data_frame = transformed_data, target_table = "cleaned_data")



# Extract data from the raw_data.csv file
raw_data = extract(file_name="raw_data.csv")

# Load the extracted_data to the raw_data table
load(data_frame=raw_data, table_name="raw_data")

# Transform data in the raw_data table
transform(
  source_table="raw_data", 
  target_table="cleaned_data"
)


def extract(file_name):
  return pd.read_csv(file_name)

def transform(data_frame):
  return data_frame.loc[:, ["industry_name", "number_of_firms"]]

def load(data_frame, file_name):
  data_frame.to_csv(file_name)
  
extracted_data = extract(file_name="raw_industry_data.csv")
transformed_data = transform(data_frame=extracted_data)

# Pass the transformed_data DataFrame to the load() function
load(data_frame=transformed_data, file_name="number_of_firms.csv")
