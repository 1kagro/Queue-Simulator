from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json

    response = {
        'data': {},
        'message': '',
        'statusCode': 200
    }
    return jsonify(response)