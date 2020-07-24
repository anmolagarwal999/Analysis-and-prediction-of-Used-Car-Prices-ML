# Here "flask" is the package name
# "Flask" is a class present im the package
from flask import Flask

#render_template is a function we are importing from the flask package
from flask import render_template

# "app" is an object of class "Flask"
'''__name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, 
and __name__ is a convenient way to tell it that'''
app = Flask(__name__)

# @app.route() creates a simple route
@app.route('/')
def index():
    return "<h1>This is basic.py file</h1>"



@app.route('/predict')
def get_data():
    







#//////////////////////////////////////////
@app.route('/information')
def info():
    return "<h1>Vought International is evil corp</h1>"
#///////////////////////////////////////////

@app.route('/hero/<name>')
def hero(name):
    #print(name)
    return f"<h1>The name of the hero is {name}</h1>"
if __name__=="__main__":
    # debug - True helps to make the real changes in code visible in the browser
    # debug -True job is to display debugging pages if an error occurs
    app.run(debug=True)