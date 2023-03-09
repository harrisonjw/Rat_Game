from flask import Flask, render_template
from game_state_manager import get_game_state, process_game_action, game_state


app = Flask(__name__)

# Basic home route
@app.route("/")
def welcome():
    return "Welcome to Rat Game!"


# gameState route displays the move count
@app.route("/gameState", methods = ["POST", "GET"])
def render_game_state():
    #return get_game_state()
    return f"moves = {game_state.move_count}"


# newGame route resets move count to zero
@app.route("/newGame", methods = ["POST", "GET"])
def new_game():
    game_state.move_count = 0
    return "starting a new game"


# action route adds +1 to the move count
@app.route("/action", methods = ["POST", "GET"])
def process_action():
    process_game_action()
    return "processing..."


# Runs the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
   



