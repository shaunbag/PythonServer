from flask import Flask, jsonify
# assign app to flask
app = Flask(__name__)


# basic root route returning a string
@app.route('/')
def home():
    return "Hello from Flask!"


# route returning json
@app.route('/json')
def get_json():
    return jsonify({"message": "Hello JSON", "items": [1,2,3]})


# route using parameter and returning in string
@app.route('/user/<name>')
def greet_user(name):
    return f"Hello, {name}!"


@app.route('/html')
def send_html():
    html = '<div><h1>HTML</h1></div>'
    return html
