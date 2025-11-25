from workspace import Workspace
from simulator import Simulator

class Toolbar:
    def __init__(self, ws: Workspace, sim: Simulator):
        self.workspace = ws
        self.simulator = sim
        self.tools = []

    def detectSelection(self):
        print("Detecting tool selection")

    def notifyAction(self, tool):
        print(f"Tool {tool} activated")
