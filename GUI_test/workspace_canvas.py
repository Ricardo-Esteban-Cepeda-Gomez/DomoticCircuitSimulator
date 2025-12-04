import tkinter as tk

class WorkspaceCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg="white")

        self.current_tool = None
        self.current_type = None

        self.canvas.bind("<Button-1>", self.on_click)

    def add_component(self, x, y, label):
        size = 50
        rect = self.canvas.create_rectangle(x, y, x+size, y+size, fill="#cce6ff")
        text = self.canvas.create_text(x+size/2, y+size/2, text=label)
        return rect, text

    def on_click(self, event):
        if self.current_tool == "component":
            self.add_component(event.x, event.y, self.current_type)