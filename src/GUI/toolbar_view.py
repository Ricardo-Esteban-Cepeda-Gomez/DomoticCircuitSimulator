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


        #import images
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
            corner_radius=5,
            command=self.main_battery_command
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

        LED_PATH = os.path.join(IMG_DIR, "led.png")

        self.led_image = ctk.CTkImage(
            light_image=Image.open(LED_PATH),
            dark_image=Image.open(LED_PATH),
        )

        self.Led_button = ctk.CTkButton(
            self.component_frame,
            image=self.led_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Led_button.pack(side="left", padx=5)
        Tooltip(self.Led_button, "LED Component")

        ALARM_PATH = os.path.join(IMG_DIR, "alarm.png")

        self.alarm_image = ctk.CTkImage(
            light_image=Image.open(ALARM_PATH),
            dark_image=Image.open(ALARM_PATH),
        )

        self.Alarm_button = ctk.CTkButton(
            self.component_frame,
            image=self.alarm_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Alarm_button.pack(side="left", padx=5)
        Tooltip(self.Alarm_button, "Alarm Component")

        PROBE_PATH = os.path.join(IMG_DIR, "probe.png")

        self.probe_image = ctk.CTkImage(
            light_image=Image.open(PROBE_PATH),
            dark_image=Image.open(PROBE_PATH),
        )

        self.Probe_button = ctk.CTkButton(
            self.other_frame,
            image=self.probe_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Probe_button.pack(side="left", padx=5)
        Tooltip(self.Probe_button, "Probe Tool")

        PAUSE_PATH = os.path.join(IMG_DIR, "pause.png")
        PLAY_PATH = os.path.join(IMG_DIR, "play.png")

        self.pause_play_image = ctk.CTkImage(
            light_image=Image.open(PAUSE_PATH),
            dark_image=Image.open(PAUSE_PATH),
        )

        self.Pause_play_button = ctk.CTkButton(
            self.other_frame,
            image=self.pause_play_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Pause_play_button.pack(side="left", padx=5)
        Tooltip(self.Pause_play_button, "Pause circuit")

        #With this command we can redraw using eigenvalues
        self.frame.pack_propagate(False)

    # ==========================================================
    # BATTERY MENU
    # ==========================================================

        self.battery_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.battery_creation_frame = ctk.CTkFrame(self.battery_frame,
                                                    fg_color="#b1b2b5",
                                                    border_color="black",
                                                    border_width=1,
                                                    corner_radius=5,
                                                    width=350)
        self.battery_creation_frame.pack_propagate(False)
        self.battery_creation_frame.pack(side="left", padx=15)
        self.battery_creation_entry = ctk.CTkEntry(self.battery_creation_frame, 
                                                    placeholder_text='battery value...', 
                                                    width=140,
                                                    height=40,
                                                    fg_color="#d2d3d6",
                                                    border_color="black",
                                                    border_width=1,
                                                    textvariable= ctk.IntVar())
        self.battery_creation_entry.pack(side="left", padx=10)

        def optionmenu_callback(choice):
            print('optionmenu dropdown clicked:', choice)
        
        optionmenu_create_battery = ctk.CTkOptionMenu(self.battery_creation_frame,
                                        values=['m', 'k','____','K','M'],
                                        width=140, 
                                        height=40,
                                        command=optionmenu_callback,
                                        fg_color="#d2d3d6",
                                        button_color="#d2d3d6",
                                        button_hover_color="#9f9fa2",
                                        dropdown_fg_color="#d2d3d6",
                                        dropdown_hover_color="#9f9fa2",
                                        text_color="black",
                                        dropdown_text_color="black",
                                        )
        optionmenu_create_battery.pack(side="left", padx=5)
        Label_V_battery = ctk.CTkLabel(self.battery_creation_frame,
                                        text='V', 
                                        fg_color='transparent',
                                        font=(None, 40))
        Label_V_battery.pack(side="right", padx=10)
        self.battery_buttons_frame = ctk.CTkFrame(self.battery_frame, fg_color="transparent")
        self.battery_buttons_frame.pack(side="right", padx=15)

        self.battery_button_create_image = ctk.CTkImage(
            light_image=Image.open(BATTERY_PATH),
            dark_image=Image.open(BATTERY_PATH),
        )

        self.Battery_button_create = ctk.CTkButton(
            self.battery_buttons_frame,
            image=self.battery_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Battery_button_create.pack(side="left", padx=5)

        self.battery_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(BATTERY_PATH).rotate(90, expand=True),
            dark_image=Image.open(BATTERY_PATH).rotate(90, expand=True),
        )

        self.Battery_button_create_rotate = ctk.CTkButton(
            self.battery_buttons_frame,
            image=self.battery_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Battery_button_create_rotate.pack(side="left", padx=5)

        BACK_PATH = os.path.join(IMG_DIR, "back.png")

        self.back_battery_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_battery = ctk.CTkButton(
            self.battery_buttons_frame,
            image=self.back_battery_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_battery_command
            )
        self.Back_battery.pack(side="left", padx=5)



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

        self.Led_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.led_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Alarm_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.alarm_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Probe_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.probe_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Pause_play_button.configure(height=new_height*0.7, width=new_height*0.7)
        self.pause_play_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Battery_button_create.configure(height=new_height*0.7, width=new_height*0.7)
        self.battery_button_create_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Battery_button_create_rotate.configure(height=new_height*0.7, width=new_height*0.7)
        self.battery_button_create_image_rotate.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.Back_battery.configure(height=new_height*0.7, width=new_height*0.7)
        self.back_battery_image.configure(size=(new_height*0.7-10, new_height*0.7-10))

        self.battery_creation_frame.configure(height=new_height*0.7)

    def main_battery_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.battery_frame.pack(side="left", padx=15)
    def back_battery_command(self):
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)
        self.battery_frame.pack_forget()
class Tooltip:
    def __init__(self, widget, text, delay=300, fade_duration=200):
        """
        fade_duration: duración en ms del fade in
        """
        self.widget = widget
        self.text = text
        self.delay = delay
        self.fade_duration = fade_duration
        self.tip_window = None
        self.after_id = None
        self.alpha = 0

        widget.bind("<Enter>", self.schedule_show)
        widget.bind("<Leave>", self.schedule_hide)

    # -------------------------
    def schedule_show(self, event=None):
        self.cancel_scheduled()
        self.after_id = self.widget.after(self.delay, self.show_tooltip)

    def schedule_hide(self, event=None):
        self.cancel_scheduled()
        self.hide_tooltip()

    def cancel_scheduled(self):
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

    # -------------------------
    def show_tooltip(self):
        if self.tip_window is not None:
            return

        x = self.widget.winfo_rootx() + 30
        y = self.widget.winfo_rooty() + 30

        self.tip_window = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = ctk.CTkLabel(
            tw,
            text=self.text,
            fg_color="#9C9C9C",
            text_color="black",
            corner_radius=6,
            padx=8,
            pady=4
        )
        label.pack()

        # Inicialmente invisible
        self.alpha = 0
        tw.attributes("-alpha", self.alpha)

        # Iniciar fade in
        self.fade_in_start_time = self.widget.winfo_toplevel().after(10, self.fade_in_step)

        # Monitorear si el mouse sigue sobre el widget
        self.check_mouse_leave()

    def fade_in_step(self):
        """Incrementa alpha hasta 1 para fade in"""
        if self.tip_window is None:
            return

        step = 0.05  # incremento de alpha
        self.alpha += step
        if self.alpha >= 1:
            self.alpha = 1
            self.tip_window.attributes("-alpha", self.alpha)
            return
        self.tip_window.attributes("-alpha", self.alpha)
        # siguiente paso en 20ms
        self.tip_window.after(20, self.fade_in_step)

    def check_mouse_leave(self):
        """Cerrar tooltip si el mouse ya no está sobre el widget."""
        if self.tip_window is None:
            return

        x, y = self.widget.winfo_pointerxy()
        if not self.widget.winfo_containing(x, y):
            self.hide_tooltip()
            return

        # sigue adentro → volver a verificar en 50ms
        self.widget.after(50, self.check_mouse_leave)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None