from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/calculator', methods=["GET"])
@swag_from({
    'tags': [
        'Calculator'
    ],
    'summary': 'Calculate net pay after tax',
    'description': 'Endpoint to calculate the net pay after a 15% tax deduction from the provided salary before tax.',
    'parameters': [
        {
            'name': 'before_tax',
            'in': 'query',
            'type': 'integer',
            'required': True,
            'description': 'Salary before tax'
        }
    ],
    'responses': {
        200: {
            'description': 'Net pay after tax',
            'schema': {
                'type': 'object',
                'properties': {
                    'pay_after_tax': {
                        'type': 'number',
                        'description': 'Net pay after 15% tax deduction'
                    }
                }
            },
            'examples': {
                'application/json': {
                    'pay_after_tax': 850
                }
            }
        },
        400: {
            'description': 'Invalid input error',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            },
            'examples': {
                'application/json': {
                    'error': 'Invalid input. Please provide a valid integer for before_tax.'
                }
            }
        }
    }
})
def net_pay():
    try:
        before_tax = int(request.args.get('before_tax'))
        tax = before_tax * 0.15
        net = before_tax - tax
        return jsonify(pay_after_tax=net)
    except (TypeError, ValueError):
        return jsonify(error="Invalid input. Please provide a valid integer for before_tax."), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




