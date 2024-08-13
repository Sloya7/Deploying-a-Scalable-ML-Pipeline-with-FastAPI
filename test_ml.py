import pytest
import pandas as pd
import numpy as np
import os



data_path = "/data/cencus.csv"
data = pd.read_csv(data_path)

train, test = train_test_split(data, random_state = 42)


#needed for test 1
from train_model import X_train, y_train, model, y_test, preds, data 

#needed for test 2
from sklearn.ensemble import RandomForestClassifier

#needed for test 3
from train_model import p, r, fb


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
    returns = [p,r,fb]
    for i in range(len(returns)):
        val = returns[i]
        assert type(val) == np.float64, "Return values not a float"
