import os

# Load environment variables (if using a .env file)
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI")

# JWT Secret Key
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
