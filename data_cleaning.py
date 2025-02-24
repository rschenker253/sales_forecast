import pandas as pd
import numpy as np

#Preprocessing function
def data_preprocessing(calendar_dataset,inventory_dataset,sales_train_dataset,sales_test_dataset):
    #Drop columns that are not neccessary
    calendar_dataset = calendar_dataset.drop(columns=["warehouse","holiday_name"])
    inventory_dataset = inventory_dataset.drop(columns=["L2_category_name_en","L3_category_name_en","L4_category_name_en","warehouse"])
    sales_train_dataset = sales_train_dataset.drop(columns=["availability"])

    #Combine the datasets into one dataset
    train_data_v2 = pd.merge(sales_train_dataset,inventory_dataset, on="unique_id", how="left")
    test_data_v2 = pd.merge(sales_test_dataset,inventory_dataset, on="unique_id", how="left")

    train_data_v3 = pd.merge(train_data_v2,calendar_dataset, on="date", how="left")
    test_data_v3 = pd.merge(test_data_v2,calendar_dataset, on="date", how="left")

    #Create new column named sell_price main for test_data
    test_data_v3["sales"] = np.nan

    print("Test_data_v3",test_data_v3.columns)

    #Create new column for solution id
    train_data_v3["solution_id"] = train_data_v3["unique_id"].astype(str) + "_" + train_data_v3["date"].astype(str)
    test_data_v3["solution_id"] = test_data_v3["unique_id"].astype(str) + "_" + test_data_v3["date"].astype(str)

    #Convert date string to datetime object
    train_data_v3["date"] = pd.to_datetime(train_data_v3["date"])
    test_data_v3["date"] = pd.to_datetime(test_data_v3["date"])

    #Create new column for year and month
    train_data_v3["month"] = train_data_v3["date"].dt.month
    train_data_v3["year"] = train_data_v3["date"].dt.year
    train_data_v3["day"] = train_data_v3["date"].dt.day

    test_data_v3["month"] = test_data_v3["date"].dt.month
    test_data_v3["year"] = test_data_v3["date"].dt.year
    test_data_v3["day"] = test_data_v3["date"].dt.day


    #Remove all missing values from sales and total_orders column
    train_data_v3.dropna(subset=["total_orders", "sales"], inplace=True)
    test_data_v3.dropna(subset=["total_orders"],inplace=True)

    # Remove all spaces in all columns with object datatype
    train_data_v3.select_dtypes(include=['object']).map(lambda x: x.strip() if isinstance(x, str) else x)
    test_data_v3.select_dtypes(include=['object']).map(lambda x: x.strip() if isinstance(x, str) else x)

    #Sort dataframe by date
    train_data_v3 = train_data_v3.sort_values(by="date")
    test_data_v3 = test_data_v3.sort_values(by="date")

    #Set date as index
    train_data_v3.set_index("date",inplace=True)
    test_data_v3.set_index("date",inplace=True)

    # Do Simple Random Sampling
    train_data_v3_sample = train_data_v3.sample(frac=0.1, random_state=42)
    test_data_v3_sample = test_data_v3.sample(frac=0.1, random_state=42)

    #Sort dataframe_sample by date
    train_data_v3_sample = train_data_v3_sample.sort_values(by="date")
    test_data_v3_sample = test_data_v3_sample.sort_values(by="date")

    #Save cleaned data as csv file in directory
    directory_train_data = r"C:\Users\user\PycharmProjects\Library\DataAnalyst\data\cleaned\cleaned_train_data.csv"
    directory_test_data = r"C:\Users\user\PycharmProjects\Library\DataAnalyst\data\cleaned\cleaned_test_data.csv"
    train_data_v3_sample.to_csv(directory_train_data)
    test_data_v3_sample.to_csv(directory_test_data)

    return train_data_v3_sample, test_data_v3_sample