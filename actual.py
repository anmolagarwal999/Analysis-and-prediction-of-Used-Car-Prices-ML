# Here "flask" is the package name
# "Flask" is a class present im the package
from flask import Flask

# render_template is a function we are importing from the flask package
from flask import render_template

#############################################################
# importing stuff
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import nltk
import pickle
########################################
from predict_value import predict_values
#########################################

# "app" is an object of class "Flask"
'''__name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, 
and __name__ is a convenient way to tell it that'''
app = Flask(__name__)

#################################################################
# specifying the excel file to be used

with open('data.pickle', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    regressor=pickle.load(f)
#print(regressor)

with open('info.pickle', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    info=pickle.load(f)
#print(info)

with open('train_cols.pickle', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    train_cols=pickle.load(f)
#print(train_cols)

with open('sc.pickle', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    sc=pickle.load(f)



# master_list=['name','power','mileage','city']

# name            Hyundai Creta 1.6 CRDi SX Option
# city                                        Pune
# year                                        2015
# kms                                        41000
# fuel                                      Diesel
# transmission                              Manual
# owner                                      First
# mileage                                    19.67
# engine                                      1582
# power                                      126.2
# seats                                          5
# price                                       12.5
# brand                                    Hyundai
# model                                      Creta


input_dict={
    "brand":["Hyundai"],
    "model":["Creta"],
    "seats":[5],
    "engine":[1582],
    "owner":["First"],
    "fuel":["Diesel"],
    "transmission":["Manual"],
    "year":[2015],
    "kms":[41000] 
    }

input_df=pd.DataFrame(input_dict)
ans=predict_values(input_df,regressor,train_cols,sc)
print(ans)

input_dict={
    "brand":["Hyundai"],
    "model":["Creta"],
    "seats":[5],
    "engine":[1582],
    "owner":["First"],
    "fuel":["Diesel"],
    "transmission":["Manual"],
    "year":[2018]   ,
        "kms":[41000] 

    }

input_df=pd.DataFrame(input_dict)
ans=predict_values(input_df,regressor,train_cols,sc)
print(ans)

input_dict={
    "brand":["Skoda"],
    "model":["Superb"],
    "seats":[5],
    "engine":[2000],
    "owner":["First"],
    "fuel":["Diesel"],
    "transmission":["Manual"],
    "year":[2012]   ,
    "kms":[4000] 

    }

input_df=pd.DataFrame(input_dict)
ans=predict_values(input_df,regressor,train_cols,sc)
print(ans)

input_dict={
    "brand":["Maruti"],
    "model":["Alto"],
    "seats":[4],
    "engine":[998],
    "owner":["First"],
    "fuel":["CNG"],
    "transmission":["Manual"],
    "year":[2014]   ,
    "kms":[40929] 

    }

input_df=pd.DataFrame(input_dict)
ans=predict_values(input_df,regressor,train_cols,sc)
print(ans)

input_dict={
    "brand":["Toyota"],
    "model":["Innova"],
    "seats":[7],
    "engine":[2393],
    "owner":["First"],
    "fuel":["Diesel"],
    "transmission":["Manual"],
    "year":[2017]   ,
    "kms":[34000] 

    }

input_df=pd.DataFrame(input_dict)
ans=predict_values(input_df,regressor,train_cols,sc)
print(ans)



#print(sc.__dict__)
#print(regressor.__dict__)





#############################################################


# # @app.route() creates a simple route
# @app.route('/')
# def index():
#     return "<h1>This is basic.py file</h1>"


# @app.route('/predict')
# def get_data():
#     pass


# @app.route('/information')
# def information():
#     return "<h1>Vought International is evil corp</h1>"
# # ///////////////////////////////////////////


# @app.route('/hero/<name>')
# def hero(name):
#     # print(name)
#     return f"<h1>The name of the hero is {name}</h1>"


# if __name__ == "__main__":
#     # debug - True helps to make the real changes in code visible in the browser
#     # debug -True job is to display debugging pages if an error occurs
#     app.run(debug=True)
