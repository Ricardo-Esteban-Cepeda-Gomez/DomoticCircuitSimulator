import customtkinter as ctk

class Menubar():
    def __init__(self, root):
        #we created the frame of the menubar
        self.frame = ctk.CTkFrame(
            root,
            height=35,
            corner_radius=0,
            fg_color="#ffffff",
            border_width=0
        )
        
        #File button
        file_button = ctk.CTkButton(hover=True)

        file_button._hover(
            
        )


        self.frame.pack(side="top", fill="x")

        self.frame.pack_propagate(False)