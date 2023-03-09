from dataclasses import dataclass

@dataclass
class GameState:
    def __init__(self, move_count):
        self.move_count = move_count

game_state = GameState(move_count = 0)

@dataclass
class GameAction:
    def __init__(self):
        pass


def get_game_state():
    return game_state

def process_game_action():
    # applies the game action to the global game state
    global game_state
    game_state.move_count += 1


 




# class GameState:
#     def __init__(self, move_count):
#         self.move_count = move_count


# class GameAction:
#     def __init__(self):
#         pass


# game_state = GameState(move_count = 0)

# def get_game_state():
#     return game_state

# def process_game_action(game_action):
#     # Applies game action to the global game state
#     pass


