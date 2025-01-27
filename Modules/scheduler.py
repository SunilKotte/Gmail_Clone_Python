from flask import Blueprint, request, jsonify
from datetime import datetime

from pymongo import MongoClient

from config import MONGO_URI

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Trigger connection test
    print("MongoDB connection successful.")
    db = client["gmail_clone"]
    users_collection = db["users"]
    tasks_collection = db["tasks"]
    
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    client = None
    db = None
    users_collection = None
    tasks_collection = None
scheduler_blueprint = Blueprint('scheduler', __name__)

@scheduler_blueprint.route('/schedule', methods=['POST'])
def schedule_meeting():
    """
    Schedule a meeting with the provided details.
    """
    data = request.json
    meeting_title = data.get('title')
    meeting_date = data.get('date')
    description = data.get('description', 'No description provided')

    try:
        # datetime.strptime(meeting_date, '%Y-%m-%d %H:%M:%S')
        tasks_collection.insert_one({"title":meeting_title,"date":meeting_date,"description":description})
        return jsonify({"message": "Meeting scheduled successfully", "date": meeting_date, "description": description}), 200
    except ValueError:
        return jsonify({"message": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"}), 400
