import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def regression_metrics(y_test, y_pred):
    """Compute metrics for model performance
    
    This function takes in series of y_test and y_pred values and computes the RMSE, MAE, R², Mean Actual, and Mean Predicted values to provide a view of performance of a regression model.
    
    Parameters
    ----------
    y_test : array-like
        An array-like object of actual values of the target variable
    y_pred : array-like
        An array-like object of predicted values of the target variable. Generally the output of model.predict(X_test)
    
    Returns
    -------
    pd.DataFrame
        A pandas dataframe with the name of the metric in the first column and the value of that metric in the second column

    Examples
    --------
    >>> calculate_stats(y_test, y_pred)
           Metric      Value
    0    RMSE     0.5234
    1     MAE     0.4123
    2      R²     0.8567
    3    Mean Actual     5.2341
    4    Mean Predicted  5.1987
    """
    # compute summary statistics
    summary = pd.DataFrame({
        'Metric': ['RMSE', 'MAE', 'R²', 'Mean Actual', 'Mean Predicted'],
        'Value': [
            np.sqrt(mean_squared_error(y_test, y_pred)),
            mean_absolute_error(y_test, y_pred),
            r2_score(y_test, y_pred),
            y_test.mean(),
            y_pred.mean()
        ]
    })
    # round for cleaner display
    summary['Value'] = summary['Value'].round(4)
    return summary