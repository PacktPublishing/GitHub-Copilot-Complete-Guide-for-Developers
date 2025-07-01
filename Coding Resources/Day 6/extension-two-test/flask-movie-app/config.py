from pymongo import MongoClient
import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/flask_movie_app')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')