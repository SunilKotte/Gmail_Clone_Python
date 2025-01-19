from flask_pymongo import PyMongo

def connect_db(app):
    mongo = PyMongo(app)
    return mongo.db