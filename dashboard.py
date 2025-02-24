import streamlit as st
import pandas as pd

st.title("?? Dashboard")

#Load cleaned data from csv file
file_path = r"C:\Users\user\PycharmProjects\Library\DataAnalyst\data\cleaned\cleaned_train_data.csv"
train_data = pd.read_csv(file_path)


#Total orders by time
#Title add later, axis straight
grouped_train_data = train_data.groupby("date")["total_orders"].sum()
st.line_chart(grouped_train_data, x_label= "Date", y_label="Total Orders")
print(grouped_train_data)

#Monthly trend over time
#Title add later, axis straight, need to sort values by descending order
grouped_train_data_month = train_data.groupby("month")["total_orders"].sum()
st.bar_chart(grouped_train_data_month)
print(grouped_train_data_month)

#Day trend over time
#Title add later, axis straight, need to sort values by descending order
grouped_train_data_day = train_data.groupby("day")["total_orders"].sum()
st.bar_chart(grouped_train_data_day,horizontal=True)
print(grouped_train_data_day)