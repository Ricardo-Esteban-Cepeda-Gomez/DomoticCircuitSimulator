import customtkinter as ctk

class Workspace():
    def __init__(self, root):
        self.root = root
        
        #we make the drawing of the Workspace like a canvas
        self.canvas = ctk.CTkCanvas(root, bg="#ffffff")
        self.canvas.pack(side="top", fill="both", expand=True)