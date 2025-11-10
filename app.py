"""
Simple Calculator API - Academic Project
A RESTful API for basic mathematical operations
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Calculator API",
        "version": "1.0.0",
        "endpoints": {
            "/add": "POST - Add two numbers",
            "/subtract": "POST - Subtract two numbers",
            "/multiply": "POST - Multiply two numbers",
            "/divide": "POST - Divide two numbers"
        }
    })

@app.route('/add', methods=['POST'])
def add():
    """Add two numbers"""
    data = request.get_json()
    try:
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        result = a + b
        return jsonify({"result": result, "operation": "addition"}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide 'a' and 'b' as numbers."}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    """Subtract two numbers"""
    data = request.get_json()
    try:
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        result = a - b
        return jsonify({"result": result, "operation": "subtraction"}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide 'a' and 'b' as numbers."}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    """Multiply two numbers"""
    data = request.get_json()
    try:
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        result = a * b
        return jsonify({"result": result, "operation": "multiplication"}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide 'a' and 'b' as numbers."}), 400

@app.route('/divide', methods=['POST'])
def divide():
    """Divide two numbers"""
    data = request.get_json()
    try:
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        result = a / b
        return jsonify({"result": result, "operation": "division"}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide 'a' and 'b' as numbers."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

