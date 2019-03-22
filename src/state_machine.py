class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.run()
        
    # Template method:
    def run_all(self, inputs):
        for i in inputs:
            print(i)
            self.current_state = self.current_state.next(i)
            self.current_state.run()
