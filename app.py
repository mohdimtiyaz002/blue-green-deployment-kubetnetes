from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "Hi, this code is developed by MOHD IMTIYAZ : 1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
