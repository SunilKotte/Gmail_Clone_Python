from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from Modules.auth import auth_blueprint
from Modules.mail_sender import mail_sender_blueprint
from Modules.scheduler import scheduler_blueprint
from Modules.file_uploader import file_uploader_blueprint
from Utils.logger import setup_logger
from flask_pymongo import PyMongo

import os
from config import MONGO_URI

# Initialize Flask app
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # Use a secure secret key

# MongoDB configuration
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
if not mongo:
    print("connecting to MongoDB")
app.config['db'] = mongo.db

# Logger setup
logger = setup_logger()

# Initialize JWT Manager
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(mail_sender_blueprint, url_prefix='/mail')
app.register_blueprint(scheduler_blueprint, url_prefix='/scheduler')
app.register_blueprint(file_uploader_blueprint, url_prefix='/upload')

@app.route("/")
def home():
    return "<h1>Welcome to Gmail!<h1>"

# Error handling
@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 Bad Request errors.
    """
    return jsonify({"message": "Bad Request", "error": str(error)}), 400

@app.errorhandler(500)
def server_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return jsonify({"message": "Internal Server Error", "error": str(error)}), 500

# Request logging
@app.before_request
def log_request_info():
    """
    Log each incoming request's method and URL.
    """
    logger.info(f"Request: {request.method} {request.url}")

if __name__ == "__main__":
    """
    Run the Flask application in debug mode.
    """
    app.run(debug=True)
