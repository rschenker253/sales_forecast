import pandas as pd
from sklearn.feature_selection import SelectKBest,f_regression,mutual_info_regression

#Calculate Correlation Coefficent with target variable (Reuse existing variable)
#Features with high correlation (positive or negative) with the target are likely to be more important.

#Univariate Feature selection (Target variable is continuous)
#Anova F-test

def p_value_evaluate(p_value):
    if p_value > 0.05:
        return "Low"
    elif 0.01 <= p_value <= 0.05:
        return "Moderate"
    else:
        return "High"

def mutual_info_evaluate(mutual_info):
    if mutual_info <= 0.1:
        return "Low"
    elif 0.1 < mutual_info <= 0.3:
        return "Moderate"
    else:
        return "High"

def anova_test(data):
    x = data.drop(columns=["sales"])
    y = data["sales"]

    selector = SelectKBest(score_func=f_regression, k='all')
    selector.fit(x,y)

    anova_scores = selector.scores_
    anova_p_values = selector.pvalues_

    anova_results = pd.DataFrame({
        "Feature" : x.columns,
        "Anova Score" : anova_scores,
        "P-Value": anova_p_values
    })

    anova_results["Level"] = anova_results["P-Value"].apply(p_value_evaluate)
    anova_results = anova_results.sort_values(by="Level", ascending=False)
    print(anova_results)

#Mutual Information
def mutual_info(data):
    x = data.drop(columns=["sales"])
    y = data["sales"]

    selector = SelectKBest(score_func=mutual_info_regression, k='all')
    selector.fit(x, y)

    mi_scores = selector.scores_

    mi_results = pd.DataFrame({
    "Feature": x.columns,
    "Mutual Info Score": mi_scores
    })

    mi_results["Level"] = mi_results["Mutual Info Score"].apply(mutual_info_evaluate)
    mi_results = mi_results.sort_values(by="Mutual Info Score", ascending=False)

    print(mi_results)