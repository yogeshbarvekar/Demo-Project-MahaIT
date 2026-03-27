"""
Simple Python Microservice using Flask
"""
from flask import Flask, jsonify, request, render_template
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    logger.info('Health check called')
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/greet', methods=['POST'])
def greet():
    """
    Greet endpoint that accepts a name in JSON request body
    """
    try:
        data = request.get_json()
        name = data.get('name', 'World') if data else 'World'
        
        logger.info(f'Greeting request received for: {name}')
        
        return jsonify({
            'message': f'Hello, {name}!',
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    except Exception as e:
        logger.error(f'Error processing greet request: {str(e)}')
        return jsonify({'error': 'Invalid request'}), 400


@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Sample data endpoint
    """
    logger.info('Data request received')
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'}
        ],
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/echo', methods=['POST'])
def echo():
    """
    Echo endpoint that returns the request body
    """
    try:
        data = request.get_json()
        logger.info(f'Echo request: {data}')
        return jsonify({
            'echo': data,
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    except Exception as e:
        logger.error(f'Error processing echo request: {str(e)}')
        return jsonify({'error': 'Invalid request'}), 400


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    logger.error(f'Internal server error: {str(error)}')
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run the Flask app
    # NOTE: In production, use a WSGI server like Gunicorn instead of Flask's development server
    app.run(host='0.0.0.0', port=5000, debug=False)


# --- UI ROUTE ---
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form.get('input', '')
        # Example: Use the greet logic for demo
        result = f'Hello, {user_input}!' if user_input else 'Hello, World!'
    return render_template('index.html', result=result)
