import customtkinter as ctk

class Toolbar:
    def __init__(self, root):
        self.root = root

        #we make the drawing of the toolbar
        self.frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#c8c8c8", height=80)
        self.frame.pack(side="top", fill="x")

        #With this command we can redraw using eigenvalues
        self.frame.pack_propagate(False)

    #we calculate the height of the toolbar
    def resize(self, event):
        new_height = max(70, int(self.root.winfo_height() / 8))
        self.frame.configure(height=new_height)
