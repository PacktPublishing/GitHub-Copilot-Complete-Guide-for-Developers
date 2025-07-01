from flask import Flask
from flask_pymongo import PyMongo
from routes.movies import movies_bp

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)

app.register_blueprint(movies_bp)

if __name__ == '__main__':
    app.run(debug=True)