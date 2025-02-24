import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def encoding(data,data_test):
    # Encode Categorical Variables
    sample_training_data_v4 = pd.get_dummies(data,columns=["warehouse", "name", "L1_category_name_en"])
    sample_testing_data = pd.get_dummies(data_test,columns=["warehouse", "name","L1_category_name_en"])
    return sample_training_data_v4,sample_testing_data


def normalization(encoded_data, encoded_test_data):
    index_data = encoded_data.index
    index_test_data = encoded_test_data.index
    print(index_data)
    print(index_test_data)
    #Normalize data using Min Max Scaling (done after the EDA)

    #Initialize MinMaxScaler
    scaler = MinMaxScaler()

    #Fit and Transform the data
    numbers_df = encoded_data.select_dtypes(include='number')
    numbers_test_df = encoded_test_data.select_dtypes(include='number')

    numbers_df = numbers_df.drop(["unique_id","product_unique_id"],axis=1)
    numbers_test_df = numbers_test_df.drop(["unique_id","product_unique_id"],axis=1)


    #Transform the data
    scaled_data = scaler.fit_transform(numbers_df)
    scaled_test_data = scaler.fit_transform(numbers_test_df)


    scaled_data_df = pd.DataFrame(scaled_data, columns=numbers_df.columns, index=index_data)
    scaled_test_data_df = pd.DataFrame(scaled_test_data , columns=numbers_test_df.columns, index=index_test_data)
    numeric_columns = encoded_data.select_dtypes(include='number').columns
    numeric_test_columns = encoded_test_data.select_dtypes(include='number').columns
    encoded_data = encoded_data.drop(numeric_columns, axis=1, inplace=True)
    encoded_test_data = encoded_test_data.drop(numeric_test_columns, axis=1, inplace=True)
    normalized_data = pd.concat([encoded_data,scaled_data_df],axis=1)
    normalized_test_data = pd.concat([encoded_test_data,scaled_test_data_df],axis=1)

    print("After Normalization")
    print(normalized_data)
    print(normalized_test_data)

    return normalized_data,normalized_test_data


