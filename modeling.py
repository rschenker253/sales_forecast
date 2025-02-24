import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
import lightgbm as lgb
from xgboost import XGBRegressor

from prophet import Prophet
#from prophet.plot import plot_plotly, plot_components_plotly
from sklearn.model_selection import TimeSeriesSplit


def model_evaluate(data,data_test):
    x_train = data.drop("sales",axis=1)
    y_train = data["sales"]
    x_test = data_test.drop("sales",axis=1)
    y_test = data_test["sales"]
    k_folds = 5
    kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)

    params = {
        'objective': 'regression',
        'metric': 'rmse',
        'boosting_type': 'gbdt',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9
    }

    models = {
    #"XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42), #okay
    #"RandomForest": RandomForestRegressor(random_state=42), #okay
    "LinearRegression": LinearRegression(),
    "Prophet": Prophet(), #issue
    }

    for model_name, model in models.items():
        scores = cross_val_score(model, x_train, y_train, cv=kf)
        mean_score = np.mean(scores)
        standard_deviation_score = np.std(scores)
        print ("Mean_Score for ",model_name,mean_score)
        print("Standard Deviation Score for ",model_name, standard_deviation_score)


#Simple Exponential Smoothing (forecasting data with no clear trend or seasonal pattern)
def ses(data,data_test):
    ses_model = SimpleExpSmoothing(data["sales"]).fit()
    forecast_ses = ses_model.forecast(len(data_test))
    print("Simple Exponential Smoothing: ",forecast_ses)
    plt.plot(data_test.index, forecast_ses, label="Forecasted Sales", color="red")
    plt.title("Simple Exponential Smoothing Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

#Holt-Winters Seasonal Model
def es(data,data_test):
    model_es = ExponentialSmoothing(data["sales"], trend=None, seasonal=None, seasonal_periods=12).fit()
    forecast_es = model_es.forecast(steps=len(data_test))
    print("Holt-Winters Seasonal Model: ", forecast_es)

    # Step 5: Plot the original data and forecast
    plt.figure(figsize=(10, 6))
    plt.plot(data_test.index,forecast_es, label='Forecast', linestyle='--')
    plt.legend()
    plt.title("Holt-Winters Seasonal Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()


# Facebook Prophet
def prophet(data,data_test):
    #Rename dataset columns from date to ds and from sales to y
    data = data["sales"].reset_index().rename(columns={'date': 'ds', 'sales': 'y'})
    data_test = data_test["sales"].reset_index().rename(columns={'date': 'ds', 'sales': 'y'})

    #Convert to datetime
    data['ds'] = pd.to_datetime(data['ds'])
    data_test['ds'] = pd.to_datetime(data_test['ds'])

    #Create Prophet Object
    model = Prophet()

    #Fit on dataset
    model.fit(data)

    #Forecast
    future = data_test[['ds']].copy()
    forecast = model.predict(future)
    print("forecast_prophet",forecast)

    # Plot the forecast
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_test['ds'], forecast['yhat'], label='Actual (Test Data)', color='orange',linewidth=2)  # add this line to plot actual values for comparison
    plt.title("Prophet Sales Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.show()

#State Space Models: Like Kalman Filters.

#Machine Learning Models: Linear Regression, Random Forest, Gradient Boosting, etc.

#Deep Learning Models: LSTM, GRU, and others.

#Cross Validation of Model

def cross_validation(train_data):
    models = {
        "RandomForest": RandomForestRegressor(),
        "LinearRegression": LinearRegression()
    }

    #How to determine the number of splits
    time_series_object = TimeSeriesSplit(n_splits=5)
    x = train_data.drop(columns=["sales"])
    y = train_data["sales"]

    for model_name, model in models.items():
        mae_scores = []
        rmse_scores = []

        for train_index, test_index in time_series_object.split(x):
            x_train, x_test = x.iloc[train_index], x.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]

            model.fit(x_train,y_train)
            y_pred = model.predict(x_test)

            mae = mean_absolute_error(y_test,y_pred)
            mse = mean_squared_error(y_test,y_pred)

            print("Mean Absolute Error (MAE):", mae)
            print("Mean Squared Error (MSE):", mse)

