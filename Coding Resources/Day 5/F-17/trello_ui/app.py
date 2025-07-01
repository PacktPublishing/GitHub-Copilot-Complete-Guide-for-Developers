from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for the Trello-like board
board_data = {
    "Backlog": ["You should add a new chat feature", "Login Issue with Hyphenated Name", "Donation Inquiry", "Newsletter Status Inquiry"],
    "To do": ["Project planning", "Kickoff meeting"],
    "Doing": [],
    "Done": ["Make videos", "You should add a new chat feature"]
}

@app.route('/')
def home():
    return render_template('index.html', board=board_data)

@app.route('/api/update_board', methods=['POST'])
def update_board():
    global board_data
    board_data = request.json
    return jsonify({"message": "Board updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
