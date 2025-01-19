from flask import Blueprint, request, jsonify
from utils.hashing import hash_password, verify_password
from utils.jwt_handler import encode_jwt
auth_blueprint = Blueprint('auth', __name__)

def get_user_by_email(db, email):
    return db.users.find_one({"email": email})

@auth_blueprint.route('/register', methods=['POST'])
def register():
    db = request.app.config['db']
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if get_user_by_email(db, email):
        return jsonify({"message": "User already exists."}), 400

    hashed_password = hash_password(password)
    db.users.insert_one({"email": email, "password": hashed_password})

    return jsonify({"message": "User registered successfully."}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    db = request.app.config['db']
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user['password']):
        return jsonify({"message": "Invalid credentials."}), 401

    token = encode_jwt({"email": email})
    return jsonify({"token": token}), 200
