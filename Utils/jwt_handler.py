import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def encode_jwt(payload):
    payload["exp"] = datetime.utcnow() + timedelta(days=1)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token.")