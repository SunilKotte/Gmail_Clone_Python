from flask import Blueprint, request, jsonify
scheduler_blueprint = Blueprint('scheduler', __name__)

@scheduler_blueprint.route('/create', methods=['POST'])
def create_meeting():
    db = request.app.config['db']
    data = request.json
    meeting_data = {
        'title': data.get('title'),
        'host': data.get('host'),
        'date': data.get('date'),
        'time': data.get('time'),
        'attendees': data.get('attendees', [])
    }
    db.meetings.insert_one(meeting_data)
    return jsonify({"message": "Meeting scheduled successfully."}), 200
