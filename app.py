from flask import Flask, render_template, request,jsonify
from utils.Exception import InvalidAPIUsage
from classes.queue import Queue
import traceback

app = Flask(__name__)

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        
        required_fields = ['lambda', 'mu', 'servers']

        for field in required_fields:
            if data.get(field) is None:
                raise InvalidAPIUsage(f'Missing field: {field}')

        response = Queue(
            data['lambda'],
            data['mu'],
            data['servers'],
            data.get('capacity', None)
        ).calculate_queue()
        
        return jsonify(response), 200
    except InvalidAPIUsage as e:
        traceback.print_exc()
        raise e
    except Exception as e:
        print(e)
        traceback.print_exc()
        raise InvalidAPIUsage(
            'Internal server error',
            status_code=500
        )