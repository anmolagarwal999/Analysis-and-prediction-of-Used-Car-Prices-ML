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
print(regressor)

with open('info.pickle', 'rb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    info=pickle.load(f)
print(info)










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
