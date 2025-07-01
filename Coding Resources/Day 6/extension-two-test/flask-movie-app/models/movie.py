from flask import current_app
from pymongo import MongoClient

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    @staticmethod
    def get_all_movies():
        client = MongoClient(current_app.config['MONGO_URI'])
        db = client['movie_database']
        movies_collection = db['movies']
        movies = movies_collection.find({}, {'_id': 0, 'title': 1})
        return [movie['title'] for movie in movies]