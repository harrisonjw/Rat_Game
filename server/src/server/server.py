from flask import Flask
from game_state_manager import get_game_state, process_game_action

app = Flask(__name__)

# Setting up a basic route
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/gameState", methods = ["GET"])
def render_game_state():
    #return get_game_state()
    return "renders the game state here"

@app.route("/newGame", methods = ["POST"])
def new_game():
    return "starting a new game"

@app.route("/action", methods = ["POST"])
def process_action():
    #return process_game_action()
    return "processing..."


# Runs the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)



