from state import State


class MainMenu (State):
    def __init__(self, window):
        self.window = window
        self.draw_buttons()
        self.draw_bg()
        self.window.update()

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
