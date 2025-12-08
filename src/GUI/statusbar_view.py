import customtkinter as ctk

class Statusbar:
    def __init__(self, root):
        self.root = root

        # We draw the status bar
        self.frame = ctk.CTkFrame(
            root, 
            fg_color="#ffffff", 
            height=50, 
            corner_radius=0, 
            border_color="#000000", 
            border_width=2
        )
        self.frame.pack(side="bottom", fill="x")

        # Prevent automatic resizing based on internal widgets
        self.frame.pack_propagate(False)

        # Text label to display information
        self.label = ctk.CTkLabel(self.frame, text="Ready", text_color="#000000")
        self.label.pack(side="left", padx=10)

    def show(self, message: str):
        """Displays any message on the status bar."""
        self.label.configure(text=message)