import pandas as pd
def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_cvs(file_name)


