import customtkinter as ctk
from PIL import Image
import os

class Toolbar:
    def __init__(self, root):
        self.root = root

        #we make the drawing of the toolbar
        self.frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#c8c8c8", border_width=0)
        self.frame.pack(side="top", fill="x")

    # ==========================================================
    # CREATE THE BUTTONS
    # ==========================================================
        botton_color="#B1B2B5"
        botton_hover_color="#555557"
        self.bee_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.bee_frame.pack(side="left", padx=10)

        self.component_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.component_frame.pack(side="left", padx=10)

        self.other_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.other_frame.pack(side="left", padx=10)


        #import image of the bee botton
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        IMG_DIR = os.path.join(BASE_DIR, "images")

        
        BEE_PATH = os.path.join(IMG_DIR, "bee.png")

        self.bee_image = ctk.CTkImage(
            light_image=Image.open(BEE_PATH),
            dark_image=Image.open(BEE_PATH),
        )

        self.Bee_button = ctk.CTkButton(
            self.bee_frame, 
            image=self.bee_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Bee_button.pack(side="left", padx=5)
        Tooltip(self.Bee_button, "Bee Tool \n This bee delete the components")

        BATTERY_PATH = os.path.join(IMG_DIR, "battery.png")

        self.battery_image = ctk.CTkImage(
            light_image=Image.open(BATTERY_PATH),
            dark_image=Image.open(BATTERY_PATH),
        )

        self.Battery_button = ctk.CTkButton(
            self.component_frame, 
            image=self.battery_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Battery_button.pack(side="left", padx=5)
        Tooltip(self.Battery_button, "Battery Component")

        RESISTOR_PATH = os.path.join(IMG_DIR, "resistor.png")

        self.resistor_image = ctk.CTkImage(
            light_image=Image.open(RESISTOR_PATH),
            dark_image=Image.open(RESISTOR_PATH),
        )

        self.Resistor_button = ctk.CTkButton(
            self.component_frame, 
            image=self.resistor_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Resistor_button.pack(side="left", padx=5)
        Tooltip(self.Resistor_button, "Resistor Component")

        SWITCH_PATH = os.path.join(IMG_DIR, "switch.png")

        self.switch_image = ctk.CTkImage(
            light_image=Image.open(SWITCH_PATH),
            dark_image=Image.open(SWITCH_PATH),
        )

        self.Switch_button = ctk.CTkButton(
            self.component_frame, 
            image=self.switch_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Switch_button.pack(side="left", padx=5)
        Tooltip(self.Switch_button, "Switch Component")

        DIODE_PATH = os.path.join(IMG_DIR, "diode.png")

        self.diode_image = ctk.CTkImage(
            light_image=Image.open(DIODE_PATH),
            dark_image=Image.open(DIODE_PATH),
        )

        self.Diode_button = ctk.CTkButton(
            self.component_frame,
            image=self.diode_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Diode_button.pack(side="left", padx=5)
        Tooltip(self.Diode_button, "Diode Component")


        #With this command we can redraw using eigenvalues
        self.frame.pack_propagate(False)
        

    #we calculate the height of the toolbar
    def resize(self, event):
        new_height = max(70, int(self.root.winfo_height() / 8))
        self.frame.configure(height=new_height)

        self.Bee_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.bee_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Battery_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.battery_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Resistor_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.resistor_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Switch_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.switch_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Diode_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.diode_image.configure(size=(new_height*0.7-10, new_height*0.7-10))


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None

        # Eventos de hover
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tip_window is not None:
            return

        x = self.widget.winfo_rootx() + 35
        y = self.widget.winfo_rooty() + 35

        # Ventana flotante
        self.tip_window = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)   # Sin bordes
        tw.wm_geometry(f"+{x}+{y}")

        # Fondo igual al tema de CTk
        label = ctk.CTkLabel(
            tw,
            text=self.text,
            fg_color="#9C9C9C",  
            text_color="black",
            bg_color="#c8c8c8",
            corner_radius=6,
            padx=8,
            pady=4
        )
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

