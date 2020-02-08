from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/quantity',methods=['POST']) # Specify app decorator. methods = ['POST']: specifies what type of http request is allowed (post:user #posts data)

def hello(): #define the function that tells flask what to do when post request sent to endpoint (/hello)
    message = request.get_json(force=True) # data (message) received from client (json: data organized into key value pairs, force ignores data type)
        S1 = message['S1']
    S2 = message['S2']
    S3 = message['S3']
    response = { #response flask sends back to the web app
        'sales_average': sales_average # key:value pair (Key is greeting : Value is hello...)
    }
    return jsonify(response) #converts the python dict to json


#start at cd (folder this code is located in)
#go to pip (command promp) and type: set FLASK_APP=sales_average.py hit enter (sales_average.py is the name of this file)
#then type: flask run --host=0.0.0.0 hit enter (to host the app locally and make it visible on the internet)
#^look into using flask waitress WSGI
#in order to find the web service: http://ipaddress:5000/quantity (type ipconfig in pip to figure out ip address: 10.1.2.147)
