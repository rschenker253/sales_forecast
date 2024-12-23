### Content Page
 - [Problem Statement](#problem-statement) 
   - [Dataset Description](#dataset-description)
   - [Columns Description](#columns-description)
   - [Evaluation](#evaluation)
   - [Submission file](#submission-file) 

***
### Problem Statement
Rohlik Group, a leading European e-grocery innovator, is revolutionising the food retail industry. We operate across 11 warehouses in Czech Republic, Germany, Austria, Hungary, and Romania. 
This challenge focuses on predicting the sales of each selected warehouse inventory for next 14 days using historical sales data.

#### Dataset Description
You are provided with historical sales data for selected Rohlik inventory and date. IDs, sales, total orders and price columns are altered to keep the real values confidential. Some features are not available in test as they are not known at the moment of making the prediction. <br>
The task is to forecast the sales column for a given id, constructed from unique_id and date (e. g. id 1226_2024-06-03 from unique_id 1226 and date 2024-06-03), for the test set.

    Datasets
    calendar.csv - calendar containing data about holidays or warehouse specific events
    inventory.csv - additional information about inventory like its product 
    sales_train.csv - training set containing the historical sales data
    sales_test.csv - full testing set
    solution.csv - full submission file in the correct format
    
> Note for datasets <br>
calendar.csv: Some columns are already in the train data but there are additional rows in this file for dates where some warehouses could be closed due to public holiday or Sunday and therefore they are not in the train set <br>
inventory.csv: Same products across all warehouses share same product unique id and name, but have different unique id

#### Columns Description
##### sales_train.csv and sales_test.csv
* unique_id - unique id for inventory
* date - date
* warehouse - warehouse name
* total_orders - historical orders for selected Rohlik warehouse
* sales - Target value, sales volume (either in pcs or kg) adjusted by availability. The sales with lower availability than 1 are already adjusted to full potential sales by Rohlik internal logic. There might be missing dates both in train and test for a given inventory due to various reasons. This column is missing in test.csv as it is target variable.
* sell_price_main - sell price
* availability - proportion of the day that the inventory was available to customers. The inventory doesn't need to be available at all times. A value of 1 means it was available for the entire day. This column is missing in test.csv as it is not known at the moment of making the prediction.
* type_0_discount, type_1_discount, … - Rohlik is running different types of promo sale actions, these show the percentage of the original price during promo ((original price - current_price) / original_price). Multiple discounts with different type can be run at the same time, but always the highest possible discount among these types is used for sales. Negative discount value should be interpreted as no discount.

##### inventory.csv
* unique_id - inventory id for a single keeping unit
* product_unique_id - product id, inventory in each warehouse has the same product unique id (same products across all warehouses has the same product id, but different unique id)
* name - inventory id for a single keeping unit
* L1_category_name, L2_category_name, … - name of the internal category, the higher the number, the more granular information is present
* warehouse - warehouse name

##### calendar.csv
* warehouse - warehouse name
* date - date
* holiday_name - name of public holiday if any holiday - 0/1 indicating the presence of holidays
* shops_closed - public holiday with most of the shops or large part of shops closed
* winter_school_holidays - winter school holidays
* school_holidays - school holidays

##### test_weights.csv
* unique_id - inventory id for a single keeping unit
* weight - weight used for final metric computation

#### Evaluation
Submissions are evaluated on Weighted Mean Absolute Error (WMAE) between the predicted sales and the actual sales. Weights for the test evaluation can be found in the Data section.

#### Submission file
For each ID in the test set, you must predict a probability for the TARGET variable. <br> 
The file should contain a header and have the following format:
| id              | sales_hat |
|-----------------|-----------|
| 840_2024-06-10  | 12.01     |
| 2317_2024-06-15 | 13.32     |
| 738_2024-06-10  | 14.12     |
| 3894_2024-06-11 | 3.03      |
| 3393_2024-06-08 | 53.03     |

***
#### Why is this important?
Accurate sales forecasts are crucial for planning process, supply chain processes, delivery logistics and inventory management. By optimizing forecasts, we can minimize waste and streamline operations, making our e-grocery services more sustainable and efficient. It will directly contribute to Rohlik mission of sustainable and efficient e-grocery delivery. Your insights will help us enhance customer service and achieve a greener future.

