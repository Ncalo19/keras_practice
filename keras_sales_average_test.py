from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/quantity',methods=['POST'])

def estimate():
    message = request.get_json(force=True)
    S1 = message['S1']
    S2 = message['S2']
    S3 = message['S3']
    sales_average = ((S1 + S2 + S3)/3)
    response = {
        'sales_average': sales_average 
    }
    return jsonify(response)
