import tkinter as tk

class PropertiesPanel:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#f5f5f5", width=200)

        tk.Label(self.frame, text="Properties", bg="#f5f5f5", font=("Arial", 12, "bold")).pack(pady=10)

        self.info = tk.Label(self.frame, text="Select a component", bg="#f5f5f5")
        self.info.pack(pady=20)
    
    def show_properties(self, component_name):
        self.info.config(text=f"Selected: {component_name}")