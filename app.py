from flask import Flask, jsonify
import requests
import argparse

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "Hi, This code for green app is develop by Mohd Imtiyaz: 2", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
