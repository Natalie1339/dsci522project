import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest
import numpy as np
from scripts.src.regression_metrics import regression_metrics
import pandas as pd

def test_regression_metrics():
    example_y_test = np.array([5.2, 6.1, 4.8, 7.3, 5.9])
    example_y_preds = np.array([5.3, 6.0, 4.9, 7.1, 6.0])

    example_result = regression_metrics(example_y_test, example_y_preds)

    # test if the result is a dataframe
    assert isinstance(example_result, pd.DataFrame)
    # test if there are nulls in the Value column
    assert not example_result['Value'].isnull().any()

