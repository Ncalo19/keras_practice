from flask import Flask #import flask class from Flask
app = Flask(__name__) #create an instance of the flask class. __name__: is the name of the application's module (__name__: used for a single 
#module)

@app.route('/sample') #tells flask what url a browser has to go to in order to run the function below it (ip address/sample)
def running():
    return 'Flask is running!'

#start at cd (folder this code is located in)
#go to pip (command promp) and type: set FLASK_APP=sample_app.py hit enter (sample_app.py is the name of this file)
#then type: flask run --host=0.0.0.0 hit enter (to host the app locally and make it visible on the internet)
#in order to find the web service: http://ipaddress:5000/sample (type ipconfig in pip to figure out ip address (10.1.2.147))

# https://www.youtube.com/watch?v=_yoxrAIf5u4&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL&index=23