class GameState:
    def __init__(self, state):
        self.state = state
        
    def __str__(self):
        return self.state
    
    def __cmp__(self, other):
        return cmp(self.state, other.state)
    
    def __hash__(self):
        return hash(self.state)

# Static fields; an enumeration of instances:
GameState.menu = GameState('menu')
GameState.game = GameState('game')
