import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

master_list=['name','power','mileage','city']

def predict_values(cars,regressor,train_cols,sc):
    #local cars2
    #cars3.head()
    cars2=cars.copy()

    #print(cars2.columns)
    #cars2=cars2.drop(master_list, axis=1)
    cars2=pd.get_dummies(cars2)
    test_cols=list(cars2.columns)
    type(test_cols)
    ######################################################################
    missing_cols = set( train_cols ) - set( test_cols )
    missing_cols2=set(test_cols)-set(train_cols)
    #print(missing_cols)
    #print(missing_cols2)
    # Add a missing column in test set with default value equal to 0
    for c in missing_cols:
        cars2[c] = 0
    # Ensure the order of column in the test set is in the same order than in train set
    cars2 =cars2[train_cols]
    #########################################################################
    X = cars2[train_cols]
    print(train_cols)

    global X_test2
    X_test = sc.transform(X)
    y_pred = regressor.predict(X_test)
    X_test2=X_test
    #print(type(y_pred))
    new_series = pd.Series(y_pred)
    cars['Random_Forest_price']=new_series
    return cars