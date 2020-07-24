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
from random_forest_doc import *
#########################################

# "app" is an object of class "Flask"
'''__name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, 
and __name__ is a convenient way to tell it that'''
app = Flask(__name__)

#################################################################
# specifying the excel file to be used
excel_file = "ideal.xlsx"
cars = pd.read_excel(excel_file)


info = {}
for i in range(len(cars)):
    brand_curr = cars["brand"][i]
    model_curr = cars["model"][i]
    info[model_curr] = brand_curr


regressor,train_cols,sc=do_random_forest(cars)
with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(regressor,f)

with open('info.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(info,f)

with open('train_cols.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(train_cols,f)

with open('sc.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(sc,f)










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
