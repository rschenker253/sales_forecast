import os
import pandas as pd

#Convert excel files format into dataframe
#Add dataframe into list
#Directory filepath does not exists
#There are no files in the folder
def load_files(directory_path):
    dataframes = []
    try:
        files_list = os.listdir(directory_path)
        if not files_list:
            raise FileNotFoundError(f"Error: The directory '{directory_path}' is empty.")
    except FileNotFoundError as e:
        print(e)
        return dataframes

    for file in files_list:
        full_file_path = os.path.join(directory_path, file)
        #print(full_file_path)
        if file.endswith("xlsx") or file.endswith("xls"):
            df = pd.read_excel(full_file_path)
            dataframes.append(df)
        elif file.endswith(".csv"):
            df = pd.read_csv(full_file_path)
            dataframes.append(df)
    return dataframes

