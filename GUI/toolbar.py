import tkinter as tk

class ToolBar:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#dddddd", height=100)

        # Wire tool
        self.wire_btn = tk.Button(self.frame, text="Delete", width=4, height=2)
        self.wire_btn.pack(pady=5, side="left")

        self.delete_btn = tk.Button(self.frame, text="selection", width=4, height=2)
        self.delete_btn.pack(pady=5, side= "left")

        # Component buttons
        self.buttons = {}
        for comp in ["Source", "Resistor", "Switch", "Capacitor", "Transistor", "LED", "Microcontroller", "Motor", "Alarm", "Screen", "Sensor"]:
            btn = tk.Button(self.frame, text=comp, width=4, height=2)
            btn.pack(pady=4, side="left")
            self.buttons[comp] = btn