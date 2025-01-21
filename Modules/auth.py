from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["gmail_clone"]
users_collection = db["users"]

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['POST'])
def register():
    """
    Handle user registration.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    
    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"email": email, "password": hashed_password})
    return jsonify({"message": "User registered successfully"}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    """
    Handle user login and return a JWT token.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid email or password"}), 401

    # token = jwt.encode({"email": user['email'], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY)
    token = create_access_token(identity=email)
    return jsonify({"token": token}), 200
