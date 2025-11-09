from workspace import workspace
from simulator import simulator
from filemanager import filemanager

class interface:
    def __init__(self, ws: workspace, sim: simulator, fm: filemanager):
        self.workspace = ws
        self.simulator = sim
        self.fileManager = fm

    def display(self):
        print("Displaying interface")

    def moveComponent(self, componentId: int, x: float, y: float):
        print(f"Moving component {componentId} to ({x}, {y})")

    def onAddComponentButton(self):
        print("Add component button pressed")

    def onConnectButton(self):
        print("Connect button pressed")

    def onStartButton(self):
        print("Start simulation")

    def onStopButton(self):
        print("Stop simulation")

    def onSaveButton(self):
        print("Save workspace")

    def onLoadButton(self):
        print("Load workspace")

    def renderUI(self):
        print("Rendering interface UI")
