from flask import Flask, render_template, request,jsonify
from utils.Exception import InvalidAPIUsage
from classes.queue import Queue

app = Flask(__name__)

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    
    data = request.json
    
    required_fields = ['lambda', 'mu', 'servers']

    for field in required_fields:
        if data.get(field) is None:
            raise InvalidAPIUsage(
                f'Missing field: {field}',
                status_code=400
            )
        

    response = Queue(
        data['lambda'],
        data['mu'],
        data['s'],
        data.get('k', None)
    ).calculate_queue()
    
    
    print(data)
    return jsonify(response), 200