from state import State


class WindowState:
    def __init__(self, state_str, state):
        self.state_str = state_str
        self.state = state
        
    def __str__(self):
        return self.state_str
    
    def __cmp__(self, other):
        return cmp(self.state_str, other.state_str)
    
    def __hash__(self):
        return hash(self.state_str)
    

class MainMenuState (State):
    def __init__(self, window):
        self.window = window

    def run(self):
        self.draw_buttons()
        self.draw_bg()
        self.window.update()

    def next(self, input):
        #### TODO Give condition to chenge to different states
        return WindowState.main_menu

    def draw_buttons(self):
        width = self.window.get_width()
        height = self.window.get_height()
        self.window.draw_string('Play', width/2, height*2/5)

    def draw_bg(self):
        self.window.set_bg_color('green')

class SettingsState (State):
    pass

class GameState (State):
    pass


