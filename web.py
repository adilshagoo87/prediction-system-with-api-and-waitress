from flask import Flask
from flask import request
import json
from flask_cors import CORS, cross_origin
import traceback
import predict
from waitress import serve

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/predict_petal_length": {"origins": "*"}})
@app.route('/predict_petal_length',methods=["GET"])
@cross_origin(origin='*',headers=['Content- Type'])
def predict_petal_length():
    try:
        petal_width = request.args.get('petal_width')
        lst= predict.function_predict(petal_width)
        resp  = json.dumps(lst[0])
        return resp
       
    except Exception:
        return traceback.format_exc()
		
@app.route("/")
def main():
    return "Welcome1"

if __name__ == "__main__":
	serve(app, host='0.0.0.0', port=8000)