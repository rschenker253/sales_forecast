from data_loading import *
from data_cleaning import *
from eda import *
from data_preprocessing import *
from modeling import *
from feature_selection import *

"""
Stuff left to do
-Computer Science Fundamentals

- git commands and building classes 
-(data pipelines, data storage, data cleaning, CI/CD, automatize everything, VCS, etc.) 
-Programming Theory
-Algo
-Data structure
-Refactor code
-Testing scripts
-Convert to API 
-Data pipeline

-Products
-Inventory Mgmt dashboard (Streamlit)
-Predictive Dashoard (Streamlit)
-Something with LLM API (Free)
-Chatbot


"""

directory_path = r"C:\Users\user\PycharmProjects\Library\DataAnalyst\data"

#Call the load_files function
dataframes_list = load_files(directory_path)

#Rename dataframe names
calendar_dataset = dataframes_list[0]
inventory_dataset = dataframes_list[1]
sales_test_dataset = dataframes_list[2]
sales_train_dataset = dataframes_list[3]
solution_dataset = dataframes_list[4]
test_weights_dataset = dataframes_list[5]

#Call data_processing function
cleaned_train_data_v3_sample, cleaned_test_data_sample = data_preprocessing(calendar_dataset,inventory_dataset,sales_train_dataset,sales_test_dataset)

#Encode Categorical Variables using One-Hot encoding
#encoded_cleaned_train_data_v3_sample,encoded_cleaned_test_data_sample = encoding(cleaned_train_data_v3_sample,cleaned_test_data_sample)

#Normalize data using Min Max Scaling
#normalized_cleaned_train_data_v3_sample, normalized_cleaned_test_data_sample = normalization(encoded_cleaned_train_data_v3_sample,encoded_cleaned_test_data_sample)




#Call correlation matrix
#correlation = correlation(cleaned_train_data_v3_sample)
#print(correlation["sales"].sort_values(ascending=False))

#Call box and whisker plot
#univariate_plot(cleaned_train_data_v3_sample,"box")

#Call density plot
#univariate_plot(cleaned_train_data_v3_sample,"hist")

#Call warehouse sales bar plot
#warehouse_sales(cleaned_train_data_v3_sample)

#Call warehouse sales trend plot
#warehouse_sales_trend(cleaned_train_data_v3_sample)

#Call Sales trend line plot
#sales_trend(cleaned_train_data_v3_sample)

#Plot bar charts to view total orders by year
#total_orders_sales_trend(cleaned_train_data_v3_sample,"year")

#Plot bar charts to view total orders by month
#total_orders_sales_trend(cleaned_train_data_v3_sample,"month")

#Plot bar charts to view total orders by day
#total_orders_sales_trend(cleaned_train_data_v3_sample,"day")

#cross_validation(normalized_cleaned_train_data_v3_sample)






#Call anova_test
#anova_test(normalized_cleaned_train_data_v3_sample)

#Call Mutual information test
#mutual_info(normalized_cleaned_train_data_v3_sample)


#model_evaluate(normalized_cleaned_train_data_v3_sample,normalized_cleaned_test_data_sample)

#Check skewness of data
#skew(encoded_cleaned_train_data_v3_sample)

#Plot boxplot
#plot_boxplot(cleaned_train_data_v3_sample)

#Model Selection for Time Series Models
#Statistical Models (Simple Exponential Smoothing)
#ses(normalized_cleaned_train_data_v3_sample, normalized_cleaned_test_data_sample)

#Holt-Winters Seasonal Model
#es(cleaned_train_data_v3_sample, normalized_cleaned_test_data_sample)

#Prophet
#prophet(normalized_cleaned_train_data_v3_sample,normalized_cleaned_test_data_sample)







