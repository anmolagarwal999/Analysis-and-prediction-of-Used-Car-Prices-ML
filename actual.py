# Here "flask" is the package name
# "Flask" is a class present im the package
# render_template is a function we are importing from the flask package
from flask import Flask,request,jsonify,render_template

from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,BooleanField, StringField, PasswordField, validators
from wtforms.validators import NumberRange,InputRequired

#############################################################
# importing stuff
import pandas as pd
import numpy as np
import pickle
########################################
from predict_value import predict_values
#########################################

# "app" is an object of class "Flask"
'''__name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, 
and __name__ is a convenient way to tell it that'''
app = Flask(__name__)
app.config['SECRET_KEY']='secret'

#################################################################
# specifying the excel file to be used

with open('data.pickle', 'rb') as f:
    regressor=pickle.load(f)

with open('info.pickle', 'rb') as f:
    info=pickle.load(f)

with open('train_cols.pickle', 'rb') as f:
    train_cols=pickle.load(f)

with open('sc.pickle', 'rb') as f:
    sc=pickle.load(f)

# input_dict1={
#     "brand":["Hyundai"],
#     "model":["Creta"],
#     "seats":[5],
#     "engine":[1582],
#     "owner":["First"],
#     "fuel":["Diesel"],
#     "transmission":["Manual"],
#     "year":[2015],
#     "kms":[41000] 
#     }

# input_df=pd.DataFrame(input_dict1)
# ans=predict_values(input_df,regressor,train_cols,sc)
#print(ans)
#############################################################

brand_set=set()
for i in info.values():
    brand_set.add(i)
brand_list=list(brand_set)
brand_list.sort()
#print(brand_list)
##########################################################
class carForm(FlaskForm):
    car_brand=SelectField('Brand',choices=[(x,x) for x in brand_list])
    car_model=SelectField('Model',choices=[],validate_choice=False)
    car_year=IntegerField("Year",validators=[NumberRange(min=1998, max=2019, message='Year should be between 1998 and 2019'),InputRequired()])
    car_kms=IntegerField("Kms",validators=[NumberRange(min=0,message='Kms driven cannot be negative'),InputRequired()])
    car_owner=SelectField('Owner Type',choices=[(x,x) for x in ['First', 'Second', 'Fourth & Above', 'Third']])
    car_transmission=SelectField('Transmission',choices=[(x,x) for x in ['Manual', 'Automatic']])
    car_fuel=SelectField('Fuel',choices=[(x,x) for x in ['Petrol', 'CNG', 'Diesel', 'LPG', 'Electric']])
    car_seats=IntegerField("Seats",validators=[NumberRange(min=2, max=12, message='Seats between 1-12'),InputRequired()])
    car_engine=IntegerField("Engine displacement (in CC)",validators=[NumberRange(min=0, message='Engine cc should be more than 0'),InputRequired()])


def getModels(brand):
    model_list=[]
    for key,val in info.items():
        if val==brand:
            model_list.append(key)
    return model_list

######################################

# @app.route() creates a simple route
@app.route('/',methods=['POST','GET'])
def index():
    form_obj=carForm()
    #print(form_obj.car_brand.choices)
    
    #print(form_obj.car_brand.data)
    if request.method=='POST' and form_obj.validate_on_submit():    
        input_dict={
        "brand":[form_obj.car_brand.data],
        "model":[form_obj.car_model.data],
        "seats":[form_obj.car_seats.data],
        "engine":[form_obj.car_engine.data],
        "owner":[form_obj.car_owner.data],
        "fuel":[form_obj.car_fuel.data],
        "transmission":[form_obj.car_transmission.data],
        "year":[form_obj.car_year.data],
        "kms":[form_obj.car_kms.data] 
        }
        form_obj.car_model.choices=getModels(form_obj.car_brand.data)

        input_df=pd.DataFrame(input_dict)
        '''NOTE THE PASS BY REFERENCE CONUNDRUM'''
       # print(input_df)
        ans=predict_values(input_df,regressor,train_cols,sc)
        #print(type(ans))
        ans=ans.to_dict();
        # print(ans)
        # print(ans["brand"][0])
        return render_template("main.html",form=form_obj,ans=ans)

    form_obj.car_brand.data="Audi"
    form_obj.car_model.choices=getModels(form_obj.car_brand.data)
    ans={"brand":"-1"}
    return render_template("main.html",form=form_obj,ans=ans)

@app.route('/brand/<company>')
def model_fetch(company):
    model_list=getModels(company)
    model_list.sort()
    return jsonify({'models_list':model_list})   

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # debug - True helps to make the real changes in code visible in the browser
    # debug -True job is to display debugging pages if an error occurs
    app.run(debug=False)
