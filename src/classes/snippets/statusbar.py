from simulator import simulator

class statusbar:
    def __init__(self, sim: simulator):
        self.simulator = sim
        self.currentMessage = ""

    def displayMessage(self, message: str):
        self.currentMessage = message
        print("Status:", message)

    def update(self, state: str):
        print("Status updated to:", state)
