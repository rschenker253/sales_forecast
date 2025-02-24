import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#Pearson's Correlatioon Coefficeint
def correlation(data):
    data = data.select_dtypes(include=["number"])
    pd.set_option('display.max_columns', None)
    correlation_matrix = data.corr("pearson")
    sns.heatmap(correlation_matrix, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()
    return correlation_matrix

def univariate_plot(data,plot_type):
    data = data.select_dtypes(include=["number"])
    data = data.drop(["unique_id","product_unique_id","year","month","day" ],axis=1)
    data.plot(kind=plot_type,subplots=True, layout=(3,5))
    plt.show()


def warehouse_sales(data):
    grouped_data = data.groupby(["warehouse"])["sales"].sum() / data['sales'].sum() * 100
    sorted_data = grouped_data.sort_values(ascending=False)
    sorted_data.plot(kind='bar')
    plt.xticks(rotation=0)
    plt.xlabel("Warehouse")
    plt.ylabel("Sales")
    plt.show()

def sales_trend(data):
    sales_data = data.groupby(data.index)["sales"].sum()
    x = np.arange(len(sales_data.index))
    y = sales_data.values
    coeffs = np.polyfit(x, y, 1)
    trendline = np.polyval(coeffs, x)
    plt.plot(sales_data.index, sales_data, linestyle='-')
    plt.plot(sales_data.index, trendline, linestyle='--')
    plt.title("Sales")
    plt.show()

def warehouse_sales_trend(data):
    grouped_data = data.groupby([data.index,"warehouse"])["sales"].sum()
    unstacked_data = grouped_data.unstack(level="warehouse")
    unstacked_data = unstacked_data.dropna()

    for warehouse in unstacked_data.columns:
        x = np.arange(len(unstacked_data.index))
        y = unstacked_data[warehouse].values
        coeffs = np.polyfit(x, y, 1)
        trendline = np.polyval(coeffs, x)

        name = warehouse + " warehouse"
        plt.plot(unstacked_data.index, unstacked_data[warehouse], label=warehouse, linestyle='-')
        plt.plot(unstacked_data.index, trendline, label='Trend Line', linestyle='--')

        plt.title(name)
        plt.show()

def total_orders_sales_trend(data,duration):
    #Total Orders (Year over Year)
    #data_filtered = data[~data["year"].isin([2020,2024])]
    total_orders = data.groupby([duration])["total_orders"].sum() / data['total_orders'].sum() * 100
    total_sales = data.groupby([duration])["sales"].sum() / data['sales'].sum() * 100
    total_orders = total_orders.sort_values(ascending=False)
    total_sales = total_sales.sort_values(ascending=False)
    bar_colors = ["teal", "steelblue", "goldenrod"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot Total Orders
    total_orders.plot(kind="bar", color=bar_colors, ax=axes[0])
    full_title = "Total Order by " + duration
    axes[0].set_xlabel(duration)
    axes[0].set_ylabel("Total Orders")
    axes[0].set_title(full_title)

    # Plot Total Sales
    total_sales.plot(kind="bar", color=bar_colors, ax=axes[1])
    full_titles = "Total Sales by " + duration
    axes[1].set_xlabel(duration)
    axes[1].set_ylabel("Total Sales")
    axes[1].set_title(full_titles)

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

def plot_bar_three(data):
    #Most popular items of all time
    total_orders_items = data.groupby(["name"])["total_orders"].sum()
    total_orders_items_sorted = total_orders_items.sort_values(ascending=False)
    top_ten_total_orders = total_orders_items_sorted.head(10)
    top_ten_total_orders.plot(kind="bar",linestyle='-', color="cyan")
    plt.xlabel("Item")
    plt.ylabel("Total Orders")
    plt.title("Total Orders by Item")
    plt.show()

def plot_bar_four(data):
    #Most least items of all time
    total_orders_items_sorted = data.tail(10)
    total_orders_items_sorted.plot(kind="bar")
    plt.xlabel("Item")
    plt.ylabel("Total Orders")
    plt.title("Total Orders by Item")
    plt.show()
