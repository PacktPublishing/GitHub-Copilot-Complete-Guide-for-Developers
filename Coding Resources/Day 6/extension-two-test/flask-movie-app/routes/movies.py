from flask import Blueprint, jsonify
from models.movie import Movie

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.objects()  # Fetch all movie documents from MongoDB
    movie_titles = [movie.title for movie in movies]  # Extract titles
    return jsonify(movie_titles)  # Return titles as JSON response