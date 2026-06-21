import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    try:
        return jsonify({
            'message': 'USL ID Management API',
            'version': '1.0.0',
            'status': 'running'
        })
    except Exception as e:
        logger.error(f'Error in index route: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health')
def health():
    try:
        return jsonify({
            'status': 'healthy',
            'service': 'USL ID Management'
        }), 200
    except Exception as e:
        logger.error(f'Error in health check: {str(e)}')
        return jsonify({'error': 'Health check failed'}), 500

@app.route('/api/version')
def version():
    try:
        return jsonify({
            'version': '1.0.0',
            'app': 'USL ID Management'
        }), 200
    except Exception as e:
        logger.error(f'Error in version route: {str(e)}')
        return jsonify({'error': 'Version check failed'}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal Server Error: {str(error)}')
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f'Unhandled exception: {str(error)}')
    return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
