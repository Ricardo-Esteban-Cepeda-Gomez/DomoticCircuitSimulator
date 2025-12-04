import customtkinter as ctk

class Statusbar:
    def __init__(self, root):
        self.root = root

        #we make the drawing of the statusbar
        self.frame = ctk.CTkFrame(root, fg_color="#ffffff", height=50, corner_radius=0, border_color="#000000", border_width=2)
        self.frame.pack(side="bottom", fill="x")

        #With this command we can redraw using eigenvalues
        self.frame.pack_propagate(False)