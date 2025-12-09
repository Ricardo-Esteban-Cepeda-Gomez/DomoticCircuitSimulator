import customtkinter as ctk

class Statusbar:
    def __init__(self, root, simulator=None):
        self.root = root
        self.simulator = simulator
        self.current_message = "Sim Status: Running"


        self.frame = ctk.CTkFrame(
            root, 
            fg_color="#ffffff", 
            height=50, 
            corner_radius=0, 
            border_color="#000000", 
            border_width=1
        )
        self.frame.pack(side="bottom", fill="x")
        self.frame.pack_propagate(False)

        self.frame_help = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_help.pack(side="left", padx=10)
        

        self.frame_state = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_state.pack(side="right", padx=10)

        self.label = ctk.CTkLabel(self.frame_state, text="Sim Status: Running", text_color="#000000")
        self.label.pack(side="left", padx=10)


    def show(self, message: str):
        self.current_message = message
        self.label.configure(text=message)   


    def update_status(self):
        if not self.simulator:
            return  

        state = "Paused" if self.simulator.running else "Running"
        self.current_message = state
        self.label.configure(text=f"Sim Status: {state}")

    def set_simulator(self, simulator):
        self.simulator = simulator