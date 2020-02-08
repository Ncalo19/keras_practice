from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__) # import app variable to create an instance of the flask class

@app.route('/hello',methods=['POST']) # Specify app decorator. methods = ['POST']: specifies what type of http request is allowed (post:user #posts data)

def hello(): #define the function that tells flask what to do when post request sent to endpoint (/hello)
    message = request.get_json(force=True) # data (message) received from client (json: data organized into key value pairs, force ignores data type)
    name = message['name'] # key labeled name in the key-value pair
    response = { #response flask sends back to the web app
        'greeting': 'Hello, ' + name + '!' + ' You are the best girlfriend a guy could ask for.' # key:value pair (Key is greeting : Value is hello...)
    }
    return jsonify(response) #converts the python dict to json


#start at cd (folder this code is located in)
#go to pip (command promp) and type: set FLASK_APP=hello_app.py hit enter (sample_app.py is the name of this file)
#then type: flask run --host=0.0.0.0 hit enter (to host the app locally and make it visible on the internet)
#^look into using flask waitress WSGI
#in order to find the web service: http://ipaddress:5000/hello (type ipconfig in pip to figure out ip address: 10.1.2.147)
