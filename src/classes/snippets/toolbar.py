from workspace import workspace
from simulator import simulator

class toolbar:
    def __init__(self, ws: workspace, sim: simulator):
        self.workspace = ws
        self.simulator = sim
        self.tools = []

    def detectSelection(self):
        print("Detecting tool selection")

    def notifyAction(self, tool):
        print(f"Tool {tool} activated")
