from flask import Blueprint, request, jsonify
mail_sender_blueprint = Blueprint('mail', __name__)

@mail_sender_blueprint.route('/send', methods=['POST'])
def send_mail():
    db = request.app.config['db']
    data = request.json
    email_data = {
        'from': data.get('from'),
        'to': data.get('to'),
        'subject': data.get('subject'),
        'body': data.get('body'),
        'attachments': data.get('attachments', [])
    }
    db.emails.insert_one(email_data)
    return jsonify({"message": "Email sent successfully."}), 200
