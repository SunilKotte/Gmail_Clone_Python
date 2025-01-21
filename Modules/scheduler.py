from flask import Blueprint, request, jsonify
from datetime import datetime

scheduler_blueprint = Blueprint('scheduler', __name__)

@scheduler_blueprint.route('/schedule', methods=['POST'])
def schedule_meeting():
    """
    Schedule a meeting with the provided details.
    """
    data = request.json
    meeting_date = data.get('date')
    description = data.get('description', 'No description provided')

    try:
        datetime.strptime(meeting_date, '%Y-%m-%d %H:%M:%S')
        return jsonify({"message": "Meeting scheduled successfully", "date": meeting_date, "description": description}), 200
    except ValueError:
        return jsonify({"message": "Invalid date format. Use YYYY-MM-DD HH:MM:SS"}), 400
