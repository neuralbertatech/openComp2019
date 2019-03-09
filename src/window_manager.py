from game_state import GameState
from window_states import MainMenuState

class WindowManager:
    def __init__(self):
        # Register the window states
        GameState.main_menu = GameState('main_menu')
        GameState.settings = GameState('settings')
        GameState.game = GameState('game')

        # Start on the main_menu state
        self.current_state = GameState.main_menu

    def run(self):
        pass
