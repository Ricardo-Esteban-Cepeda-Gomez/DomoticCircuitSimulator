import tkinter as tk
from menubar import MenuBar
from toolbar import ToolBar
from workspace_canvas import WorkspaceCanvas
from properties_panel import PropertiesPanel
from statusbar import StatusBar
from controller import Controller
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x700")
        self.root.title("BeeSmart")

        # Menu bar
        self.menu = MenuBar(self.root)

        # TOP TOOLBAR
        self.toolbar = ToolBar(self.root)
        self.toolbar.frame.pack(side="top", fill="x")

        # RIGHT PROPERTIES PANEL
        self.properties = PropertiesPanel(self.root)
        self.properties.frame.pack(side="right", fill="y")

        # LEFT CONTAINER (workspace + status bar)
        self.left_container = tk.Frame(self.root)
        self.left_container.pack(side="left", fill="both", expand=True)

        # WORKSPACE inside left container
        self.workspace = WorkspaceCanvas(self.left_container)
        self.workspace.canvas.pack(side="top", fill="both", expand=True)

        # STATUS BAR inside left container (below workspace)
        self.status = StatusBar(self.left_container)
        self.status.frame.pack(side="bottom", fill="x")

        # Controller
        #self.controller = Controller(self.toolbar, self.workspace, self.properties, self.status)

    def run(self):
        self.root.mainloop()
