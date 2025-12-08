from workspace import Workspace

class Simulator:
    def __init__(self, ws: Workspace):

        self.workspace = ws

        self.time_step = 0.0

        self.running = False

    def toggle(self):
        self.running = not self.running
        print(f"Simulation running: {self.running}")

    def update(self):
        print("Simulation updated")

    def run_step(self, dt: float = 1.0):
        if not self.running:
            print("Simulation paused - step ignored")
            return
        
        self.time_step += dt
        print(f"Simulation time: {self.time_step}")
        self.update()
