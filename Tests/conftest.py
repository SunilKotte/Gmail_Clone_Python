import pytest
from app import create_app
from pymongo import MongoClient
from config import MONGO_URI
import werkzeug

@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app()  # Replace with your create_app() function
    app.config['TESTING'] = True  # Enable testing mode
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for easier testing, if applicable
    return app

@pytest.fixture
def client(app):
    """
    Provide a test client for making requests to the app.
    """
    return app.test_client()

@pytest.fixture
def mongo_client():
    """
    Set up a test MongoDB client.
    """
    client = MongoClient(MONGO_URI)
    db = client["gmail_clone_test"]  # Use a test database
    yield db
    client.drop_database("gmail_clone_test")  # Clean up after tests
