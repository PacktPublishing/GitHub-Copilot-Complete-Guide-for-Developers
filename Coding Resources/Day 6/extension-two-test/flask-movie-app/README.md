# Flask Movie App

This is a simple Flask application that retrieves movie titles from a MongoDB database and displays them on a web page.

## Project Structure

```
flask-movie-app
├── app.py                # Entry point of the application
├── requirements.txt      # Project dependencies
├── config.py             # Configuration settings
├── models
│   └── movie.py         # Movie model for MongoDB
├── routes
│   └── movies.py        # Routes for movie-related requests
├── templates
│   └── index.html       # HTML template for displaying movie titles
├── static
│   ├── css
│   │   └── style.css    # CSS styles for the application
│   └── js
│       └── script.js     # JavaScript for client-side functionality
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-movie-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure MongoDB:**
   Update the `config.py` file with your MongoDB connection URI.

5. **Run the application:**
   ```
   python app.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

Once the application is running, it will fetch movie titles from the MongoDB database and display them on the main page. You can modify the database entries to see different titles.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.