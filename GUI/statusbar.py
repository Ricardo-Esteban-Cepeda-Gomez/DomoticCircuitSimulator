import tkinter as tk

class StatusBar:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#e6e6e6")
        self.label = tk.Label(self.frame, text="Ready", bg="#e6e6e6")
        self.label.pack(side="left", padx=10)

    def update(self, msg):
        self.label.config(text=msg)