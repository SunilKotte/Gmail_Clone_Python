# app.py
from flask import Flask
from modules.auth import auth_blueprint
from modules.mail_sender import mail_sender_blueprint
from modules.scheduler import scheduler_blueprint
from config import connect_db

app = Flask(__name__)

# MongoDB Connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/gmail_clone'
db = connect_db(app)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(mail_sender_blueprint, url_prefix='/mail')
app.register_blueprint(scheduler_blueprint, url_prefix='/schedule')

if __name__ == "__main__":
    app.run(debug=True)