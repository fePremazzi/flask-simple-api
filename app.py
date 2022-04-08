import numpy as np
from flask import Flask, jsonify, request

# initialize our Flask application
app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def setName():
    if request.method=='GET':        
        return jsonify({"label": "0", "predict": "0.654986521"})


if __name__=='__main__':
    app.run(debug=True, port=8888, host="0.0.0.0")