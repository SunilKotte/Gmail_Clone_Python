import os

# Load environment variables (if using a .env file)
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sunilcoviet:95112369@cluster0.7nc2r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# JWT Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "your_jwt_secret_key")
