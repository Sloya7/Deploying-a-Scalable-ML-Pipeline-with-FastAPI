import pytest
import pandas as pd
import numpy as np
from train_model import X_train, y_train, model, y_test, preds
from ml.model import compute_model_metrics
from sklearn.ensemble import RandomForestClassifier

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_data_NAs():
    """
    Testing if training data has any NA values
    """
    assert pd.isna(X_train).all() == 0, "X_train has NA values"
    assert pd.isna(y_train).all() == 0, "y_train has NA values"



# TODO: implement the second test. Change the function name and input as needed
def test_model_type():
    """
    Check that the model is a RandomForestClassier model
    """
    
    assert str(model) == 'RandomForestClassifier()', "Wrong Model type being used"


# TODO: implement the third test. Change the function name and input as needed
def test_compute_metics_floats():
    """
    Ensure that the compute model metrics function returns 3 floats
    """
    returns = compute_model_metrics(y_test, preds)
    assert len(returns) == 3, "Returned length of compute_model_metrics incorrect"
    for i in range(len(returns)):
        val = returns[i]
        assert type(val) == np.float64, ("Return values not a float")