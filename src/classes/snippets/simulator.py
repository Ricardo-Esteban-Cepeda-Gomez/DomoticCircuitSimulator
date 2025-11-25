from workspace import Workspace

class Simulator:
    def __init__(self, ws: workspace):
        self.workspace = ws
        self.time_step = 0.0

    def toggle(self):
        print("Simulation toggled")

    def update(self):
        print("Simulation updated")
