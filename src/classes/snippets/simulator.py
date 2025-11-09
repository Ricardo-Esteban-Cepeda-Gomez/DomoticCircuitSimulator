from workspace import workspace

class simulator:
    def __init__(self, ws: workspace):
        self.workspace = ws
        self.timeStep = 0.0

    def toggle(self):
        print("Simulation toggled")

    def update(self):
        print("Simulation updated")
