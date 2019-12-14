from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route('/dth')
def hello_world():
    with open("temp.txt", "r") as file:
        temp = ""
        for line in file.readlines():
            temp = line
            break
        print(temp)
    temp = temp.replace("$","")
    return jsonify(temp)
