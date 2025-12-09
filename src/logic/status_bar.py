from simulator import Simulator

class Statusbar:
    def __init__(self, sim: Simulator):
        self.simulator = sim
        self.current_message = ""

    def displayMessage(self, message: str):
        self.current_message = message
        print("Status:", message)

    def update(self):
        state = "Paused" if self.simulator.is_paused else "Running"
        self.current_message = state
        print("Status:", state)
