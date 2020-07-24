import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import r2_score
#y_train=np.array([[1],[2],[3]])
#y_pred=y_train





def do_random_forest(cars):
    cars2=cars.copy()

    # columns to be dropped
    master_list=['name','power','mileage','city']
    cars2=cars2.drop(master_list, axis=1)

    cars2=pd.get_dummies(cars2)
    col_now=list(cars2.columns)
    col_now.remove("price")
    train_cols=col_now
    print(train_cols)

    X = cars2[col_now]
    y = cars2['price']

    # split into train and test sets
    '''Since this is the training set and the testing set is being explicitly exported below,
    so for checking purposes, the initial training set is being reduced to just 0.0005 of the original size'''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0005, random_state=36062)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)   
    regressor = RandomForestRegressor(n_estimators=100, random_state=3231)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)   
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred))) 
    coeff = r2_score(y_test, y_pred)
    print(coeff)
    print(type(regressor))
    return regressor,train_cols,sc

