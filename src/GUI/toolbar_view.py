import customtkinter as ctk
from PIL import Image
import os

class Toolbar:
    def __init__(self, root):
        self.root = root
        self.controller = None

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
            corner_radius=5,
            command=lambda: self.main("bee", 0, 0)
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
            corner_radius=5,
            command=self.main_resistor_command
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
            corner_radius=5,
            command=self.main_switch_command
            )
        self.Switch_button.pack(side="left", padx=5)
        Tooltip(self.Switch_button, "Switch Component")

        CAPACITOR_PATH = os.path.join(IMG_DIR, "capacitor.png")

        self.capacitor_image = ctk.CTkImage(
            light_image=Image.open(CAPACITOR_PATH),
            dark_image=Image.open(CAPACITOR_PATH),
        )

        self.Capacitor_button = ctk.CTkButton(
            self.component_frame,
            image=self.capacitor_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.main_capacitor_command
            )
        self.Capacitor_button.pack(side="left", padx=5)
        Tooltip(self.Capacitor_button, "Capacitor Component")

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
            corner_radius=5,
            command=self.main_led_command
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
            corner_radius=5,
            command=self.main_alarm_command
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
            corner_radius=5,
            command=self.main_probe_command
            )
        self.Probe_button.pack(side="left", padx=5)
        Tooltip(self.Probe_button, "Probe Tool")

        PAUSE_PATH = os.path.join(IMG_DIR, "pause.png")
        PLAY_PATH = os.path.join(IMG_DIR, "play.png")

        self.pause_image = ctk.CTkImage(
            light_image=Image.open(PAUSE_PATH),
            dark_image=Image.open(PAUSE_PATH),
        )

        self.play_image = ctk.CTkImage(
            light_image=Image.open(PLAY_PATH),
            dark_image=Image.open(PLAY_PATH),
        )

        def toogled_image():
            if self.Pause_play_button.cget("image") == self.pause_image:
                self.Pause_play_button.configure(image=self.play_image)
                self.main("pause", 0, 0)
            else:
                self.Pause_play_button.configure(image=self.pause_image)
                self.main("play", 0, 0)

        self.Pause_play_button = ctk.CTkButton(
            self.other_frame,
            image=self.pause_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=toogled_image
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
                                                    width=300)
        self.battery_creation_frame.pack_propagate(False)
        self.battery_creation_frame.pack(side="left", padx=15)

        self.first_battery_value = ctk.StringVar()
        self.battery_value = 0.0
        self.selected_unit_battery = ctk.StringVar(value="____")

        def recalc_value_battery(*args):
            value_str = self.first_battery_value.get()
            unit = self.selected_unit_battery.get()

            try:
                value = float(value_str)
            except ValueError:
                Tooltip(self.battery_creation_frame, "coloca un valor valido").show_tooltip()
                return

            if value <= 0:
                return

            if unit == 'μ':
                self.battery_value = value * 1e-6
            elif unit == 'm':
                self.battery_value = value * 1e-3
            elif unit == '____':
                self.battery_value = value
            elif unit == 'K':
                self.battery_value = value * 1e3
            elif unit == 'M':
                self.battery_value = value * 1e6
            print("Battery final value:", self.battery_value)

        self.battery_creation_entry = ctk.CTkEntry(self.battery_creation_frame, 
                                                    placeholder_text='battery value...', 
                                                    width=100,
                                                    height=40,
                                                    fg_color="#d2d3d6",
                                                    border_color="black",
                                                    text_color="black",
                                                    border_width=1,
                                                    textvariable= self.first_battery_value,)
        self.battery_creation_entry.pack(side="left", padx=10)
        
        self.first_battery_value.trace_add("write", recalc_value_battery)
        
        optionmenu_create_battery = ctk.CTkOptionMenu(self.battery_creation_frame,
                                        values=['μ', 'm','____','K','M'],
                                        width=100, 
                                        height=40,
                                        command=lambda choice: (self.selected_unit_battery.set(choice), recalc_value_battery()),
                                        fg_color="#d2d3d6",
                                        button_color="#d2d3d6",
                                        button_hover_color="#9f9fa2",
                                        dropdown_fg_color="#d2d3d6",
                                        dropdown_hover_color="#9f9fa2",
                                        text_color="black",
                                        dropdown_text_color="black",
                                        variable=self.selected_unit_battery
                                        )
        optionmenu_create_battery.pack(side="left", padx=5)
        optionmenu_create_battery.set("____")
        Label_V_battery = ctk.CTkLabel(self.battery_creation_frame,
                                        text='V', 
                                        fg_color='transparent',
                                        font=(None, 40),
                                        text_color="black",
                                        width=30)
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
            corner_radius=5,
            command=lambda: self.main("battery", self.battery_value, 0)
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
            corner_radius=5,
            command=lambda: self.main("battery_rotate", self.battery_value, 0)
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
    # ==========================================================
    # RESISTOR MENU
    # ==========================================================
        self.resistor_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.resistor_creation_frame = ctk.CTkFrame(self.resistor_frame,
                                                    fg_color="#b1b2b5",
                                                    border_color="black",
                                                    border_width=1,
                                                    corner_radius=5,
                                                    width=300)
        self.resistor_creation_frame.pack_propagate(False)
        self.resistor_creation_frame.pack(side="left", padx=15)

        self.first_resistor_value = ctk.StringVar()
        self.resistor_value = 0.0
        self.selected_unit_resistor = ctk.StringVar(value="____")

        def recalc_value_resistor(*args):
            value_str = self.first_resistor_value.get()
            unit = self.selected_unit_resistor.get()

            try:
                value = float(value_str)
            except ValueError:
                Tooltip(self.resistor_creation_frame, "coloca un valor valido").show_tooltip()
                return

            if value <= 0:
                return

            if unit == 'μ':
                self.resistor_value = value * 1e-6
            elif unit == 'm':
                self.resistor_value = value * 1e-3
            elif unit == '____':
                self.resistor_value = value
            elif unit == 'K':
                self.resistor_value = value * 1e3
            elif unit == 'M':
                self.resistor_value = value * 1e6
            print("Resistor final value:", self.resistor_value)

        self.resistor_creation_entry = ctk.CTkEntry(self.resistor_creation_frame, 
                                                    placeholder_text='resistor value...', 
                                                    width=100,
                                                    height=40,
                                                    fg_color="#d2d3d6",
                                                    border_color="black",
                                                    text_color="black",
                                                    border_width=1,
                                                    textvariable= self.first_resistor_value,)
        self.resistor_creation_entry.pack(side="left", padx=10)
        
        self.first_resistor_value.trace_add("write", recalc_value_resistor)
        
        optionmenu_create_resistor = ctk.CTkOptionMenu(self.resistor_creation_frame,
                                        values=['μ', 'm','____','K','M'],
                                        width=100, 
                                        height=40,
                                        command=lambda choice: (self.selected_unit_resistor.set(choice), recalc_value_resistor()),
                                        fg_color="#d2d3d6",
                                        button_color="#d2d3d6",
                                        button_hover_color="#9f9fa2",
                                        dropdown_fg_color="#d2d3d6",
                                        dropdown_hover_color="#9f9fa2",
                                        text_color="black",
                                        dropdown_text_color="black",
                                        variable=self.selected_unit_resistor
                                        )
        optionmenu_create_resistor.pack(side="left", padx=5)
        optionmenu_create_resistor.set("____")
        Label_ohm_resistor = ctk.CTkLabel(self.resistor_creation_frame,
                                        text='Ω', 
                                        fg_color='transparent',
                                        font=(None, 40),
                                        text_color="black",
                                        width=30)
        Label_ohm_resistor.pack(side="right", padx=10)
        self.resistor_buttons_frame = ctk.CTkFrame(self.resistor_frame, fg_color="transparent")
        self.resistor_buttons_frame.pack(side="right", padx=15)

        self.resistor_button_create_image = ctk.CTkImage(
            light_image=Image.open(RESISTOR_PATH),
            dark_image=Image.open(RESISTOR_PATH),
        )

        self.Resistor_button_create = ctk.CTkButton(
            self.resistor_buttons_frame,
            image=self.resistor_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("resistor", self.resistor_value, 0)
            )
        self.Resistor_button_create.pack(side="left", padx=5)

        self.resistor_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(RESISTOR_PATH).rotate(90, expand=True),
            dark_image=Image.open(RESISTOR_PATH).rotate(90, expand=True),
        )

        self.Resistor_button_create_rotate = ctk.CTkButton(
            self.resistor_buttons_frame,
            image=self.resistor_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("resistor_rotate", self.resistor_value, 0)
            )
        self.Resistor_button_create_rotate.pack(side="left", padx=5)

        self.back_resistor_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_resistor = ctk.CTkButton(
            self.resistor_buttons_frame,
            image=self.back_resistor_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_resistor_command
            )
        self.Back_resistor.pack(side="left", padx=5)
    # ==========================================================
    # SWITCH MENU
    # ==========================================================
        self.switch_frame = ctk.CTkFrame(self.frame, fg_color="transparent")

        self.switch_buttons_frame = ctk.CTkFrame(self.switch_frame, fg_color="transparent")
        self.switch_buttons_frame.pack(side="right", padx=15)

        self.switch_button_create_image = ctk.CTkImage(
            light_image=Image.open(SWITCH_PATH),
            dark_image=Image.open(SWITCH_PATH),
        )

        self.Switch_button_create = ctk.CTkButton(
            self.switch_buttons_frame,
            image=self.switch_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("switch", 0, 0)
            )
        self.Switch_button_create.pack(side="left", padx=5)

        self.switch_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(SWITCH_PATH).rotate(90, expand=True),
            dark_image=Image.open(SWITCH_PATH).rotate(90, expand=True),
        )

        self.Switch_button_create_rotate = ctk.CTkButton(
            self.switch_buttons_frame,
            image=self.switch_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("switch_rotate", 0, 0)
            )
        self.Switch_button_create_rotate.pack(side="left", padx=5)

        self.back_switch_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_switch = ctk.CTkButton(
            self.switch_buttons_frame,
            image=self.back_switch_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_switch_command
            )
        self.Back_switch.pack(side="left", padx=5)
    # ==========================================================
    # CAPACITOR MENU
    # ==========================================================
        self.capacitor_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.capacitor_creation_frame = ctk.CTkFrame(self.capacitor_frame,
                                                    fg_color="#b1b2b5",
                                                    border_color="black",
                                                    border_width=1,
                                                    corner_radius=5,
                                                    width=300)
        self.capacitor_creation_frame.pack_propagate(False)
        self.capacitor_creation_frame.pack(side="left", padx=15)

        self.first_capacitor_value = ctk.StringVar()
        self.capacitor_value = 0.0
        self.selected_unit_capacitor = ctk.StringVar(value="____")

        def recalc_value_capacitor(*args):
            value_str = self.first_capacitor_value.get()
            unit = self.selected_unit_capacitor.get()

            try:
                value = float(value_str)
            except ValueError:
                Tooltip(self.capacitor_creation_frame, "coloca un valor valido").show_tooltip()
                return

            if value <= 0:
                return

            if unit == 'μ':
                self.capacitor_value = value * 1e-6
            elif unit == 'm':
                self.capacitor_value = value * 1e-3
            elif unit == '____':
                self.capacitor_value = value
            elif unit == 'K':
                self.capacitor_value = value * 1e3
            elif unit == 'M':
                self.capacitor_value = value * 1e6
            print("Capacitor final value:", self.capacitor_value)

        self.capacitor_creation_entry = ctk.CTkEntry(self.capacitor_creation_frame, 
                                                    placeholder_text='capacitor value...', 
                                                    width=100,
                                                    height=40,
                                                    fg_color="#d2d3d6",
                                                    border_color="black",
                                                    text_color="black",
                                                    border_width=1,
                                                    textvariable= self.first_capacitor_value,)
        self.capacitor_creation_entry.pack(side="left", padx=10)
        
        self.first_capacitor_value.trace_add("write", recalc_value_capacitor)
        
        optionmenu_create_capacitor = ctk.CTkOptionMenu(self.capacitor_creation_frame,
                                        values=['μ', 'm','____','K','M'],
                                        width=100, 
                                        height=40,
                                        command=lambda choice: (self.selected_unit_capacitor.set(choice), recalc_value_capacitor()),
                                        fg_color="#d2d3d6",
                                        button_color="#d2d3d6",
                                        button_hover_color="#9f9fa2",
                                        dropdown_fg_color="#d2d3d6",
                                        dropdown_hover_color="#9f9fa2",
                                        text_color="black",
                                        dropdown_text_color="black",
                                        variable=self.selected_unit_capacitor
                                        )
        optionmenu_create_capacitor.pack(side="left", padx=5)
        optionmenu_create_capacitor.set("____")
        Label_volt_capacitor = ctk.CTkLabel(self.capacitor_creation_frame,
                                        text='V', 
                                        fg_color='transparent',
                                        font=(None, 40),
                                        text_color="black",
                                        width=30)
        Label_volt_capacitor.pack(side="right", padx=10)

        self.capacitor_creation_frame_F = ctk.CTkFrame(self.capacitor_frame,
                                                    fg_color="#b1b2b5",
                                                    border_color="black",
                                                    border_width=1,
                                                    corner_radius=5,
                                                    width=300)
        self.capacitor_creation_frame_F.pack_propagate(False)
        self.capacitor_creation_frame_F.pack(side="left", padx=15)

        self.first_capacitor_F_value = ctk.StringVar()
        self.capacitor_F_value = 0.0
        self.selected_unit_capacitor_F = ctk.StringVar(value="____")

        def recalc_value_capacitor_F(*args):
            value_str = self.first_capacitor_F_value.get()
            unit = self.selected_unit_capacitor_F.get()

            try:
                value = float(value_str)
            except ValueError:
                Tooltip(self.capacitor_creation_frame_F, "coloca un valor valido").show_tooltip()
                return

            if value <= 0:
                return

            if unit == 'μ':
                self.capacitor_F_value = value * 1e-6
            elif unit == 'm':
                self.capacitor_F_value = value * 1e-3
            elif unit == '____':
                self.capacitor_F_value = value
            print("Capacitor final value:", self.capacitor_F_value)

        self.capacitor_F_creation_entry = ctk.CTkEntry(self.capacitor_creation_frame_F, 
                                                    placeholder_text='capacitor value...', 
                                                    width=100,
                                                    height=40,
                                                    fg_color="#d2d3d6",
                                                    border_color="black",
                                                    text_color="black",
                                                    border_width=1,
                                                    textvariable= self.first_capacitor_F_value,)
        self.capacitor_F_creation_entry.pack(side="left", padx=10)
        
        self.first_capacitor_F_value.trace_add("write", recalc_value_capacitor_F)
        
        optionmenu_create_capacitor_F = ctk.CTkOptionMenu(self.capacitor_creation_frame_F,
                                        values=['μ', 'm','____'],
                                        width=100, 
                                        height=40,
                                        command=lambda choice: (self.selected_unit_capacitor_F.set(choice), recalc_value_capacitor_F()),
                                        fg_color="#d2d3d6",
                                        button_color="#d2d3d6",
                                        button_hover_color="#9f9fa2",
                                        dropdown_fg_color="#d2d3d6",
                                        dropdown_hover_color="#9f9fa2",
                                        text_color="black",
                                        dropdown_text_color="black",
                                        variable=self.selected_unit_capacitor_F
                                        )
        optionmenu_create_capacitor_F.pack(side="left", padx=5)
        optionmenu_create_capacitor_F.set("____")
        Label_volt_capacitor_F = ctk.CTkLabel(self.capacitor_creation_frame_F,
                                        text='F', 
                                        fg_color='transparent',
                                        font=(None, 40),
                                        text_color="black",
                                        width=30)
        Label_volt_capacitor_F.pack(side="right", padx=10)

        self.capacitor_buttons_frame = ctk.CTkFrame(self.capacitor_frame, fg_color="transparent")
        self.capacitor_buttons_frame.pack(side="right", padx=15)

        self.capacitor_button_create_image = ctk.CTkImage(
            light_image=Image.open(CAPACITOR_PATH),
            dark_image=Image.open(CAPACITOR_PATH),
        )

        self.Capacitor_button_create = ctk.CTkButton(
            self.capacitor_buttons_frame,
            image=self.capacitor_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("capacitor", self.capacitor_value, self.capacitor_F_value)
            )
        self.Capacitor_button_create.pack(side="left", padx=5)

        self.capacitor_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(CAPACITOR_PATH).rotate(90, expand=True),
            dark_image=Image.open(CAPACITOR_PATH).rotate(90, expand=True),
        )

        self.Capacitor_button_create_rotate = ctk.CTkButton(
            self.capacitor_buttons_frame,
            image=self.capacitor_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("capacitor_rotate", self.capacitor_value, self.capacitor_F_value)
            )
        self.Capacitor_button_create_rotate.pack(side="left", padx=5)

        self.back_capacitor_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_capacitor = ctk.CTkButton(
            self.capacitor_buttons_frame,
            image=self.back_capacitor_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_capacitor_command
            )
        self.Back_capacitor.pack(side="left", padx=5)
    # ==========================================================
    # LED MENU
    # ==========================================================
        self.led_frame = ctk.CTkFrame(self.frame, fg_color="transparent")

        self.led_buttons_frame = ctk.CTkFrame(self.led_frame, fg_color="transparent")
        self.led_buttons_frame.pack(side="right", padx=15)

        self.led_button_create_image = ctk.CTkImage(
            light_image=Image.open(LED_PATH),
            dark_image=Image.open(LED_PATH),
        )

        self.Led_button_create = ctk.CTkButton(
            self.led_buttons_frame,
            image=self.led_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command= lambda: self.main("led", 0, 0)
            )
        self.Led_button_create.pack(side="left", padx=5)

        self.led_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(LED_PATH).rotate(90, expand=True),
            dark_image=Image.open(LED_PATH).rotate(90, expand=True),
        )

        self.Led_button_create_rotate = ctk.CTkButton(
            self.led_buttons_frame,
            image=self.led_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=lambda: self.main("led_rotate", 0, 0)
            )
        self.Led_button_create_rotate.pack(side="left", padx=5)

        self.back_led_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_led = ctk.CTkButton(
            self.led_buttons_frame,
            image=self.back_led_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_led_command
            )
        self.Back_led.pack(side="left", padx=5)
    # ==========================================================
    # ALARM MENU
    # ==========================================================
        self.alarm_frame = ctk.CTkFrame(self.frame, fg_color="transparent")

        self.alarm_checkbox_frame= ctk.CTkFrame(self.alarm_frame,
                                                width=100,
                                                fg_color="#b1b2b5",
                                                border_color="black",
                                                border_width=1,
                                                corner_radius=5)
        self.alarm_checkbox_frame.pack(side="left")

        self.dc_ac=True

        def alarm_dc_checkbox_event():
            self.alarm_ac_checkbox.deselect()
            self.dc_ac=True
        
        check_var_dc = ctk.BooleanVar(value=True)
        self.alarm_dc_checkbox = ctk.CTkCheckBox(self.alarm_checkbox_frame, 
                                                text='DC', 
                                                command=alarm_dc_checkbox_event,
                                                width=40, 
                                                height=20, 
                                                checkbox_width=15, 
                                                checkbox_height=15,
                                                variable=check_var_dc, 
                                                onvalue=True, 
                                                offvalue=False,
                                                border_width=1,
                                                border_color="black",
                                                text_color="black",
                                                font=(None, 20))
        self.alarm_dc_checkbox.pack(side="top", pady=1)

        def alarm_ac_checkbox_event():
            self.alarm_dc_checkbox.deselect()
            self.dc_ac=False

        
        check_var_ac = ctk.BooleanVar(value=False)
        self.alarm_ac_checkbox = ctk.CTkCheckBox(self.alarm_checkbox_frame, 
                                                text='AC', 
                                                command=alarm_ac_checkbox_event,
                                                width=40, 
                                                height=20, 
                                                checkbox_width=15, 
                                                checkbox_height=15,
                                                variable=check_var_ac, 
                                                onvalue=True, 
                                                offvalue=False,
                                                border_width=1,
                                                border_color="black",
                                                text_color="black",
                                                font=(None, 20))
        self.alarm_ac_checkbox.pack(side="top", pady=1)



        self.alarm_buttons_frame = ctk.CTkFrame(self.alarm_frame, fg_color="transparent")
        self.alarm_buttons_frame.pack(side="right", padx=15)

        self.alarm_button_create_image = ctk.CTkImage(
            light_image=Image.open(ALARM_PATH),
            dark_image=Image.open(ALARM_PATH),
        )

        self.Alarm_button_create = ctk.CTkButton(
            self.alarm_buttons_frame,
            image=self.alarm_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command= lambda: self.main("Alarm", self.dc_ac, 0)
            )
        self.Alarm_button_create.pack(side="left", padx=5)

        self.alarm_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(ALARM_PATH).rotate(90, expand=True),
            dark_image=Image.open(ALARM_PATH).rotate(90, expand=True),
        )

        self.Alarm_button_create_rotate = ctk.CTkButton(
            self.alarm_buttons_frame,
            image=self.alarm_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command= lambda: self.main("Alarm_rotate", self.dc_ac, 0)
            )
        self.Alarm_button_create_rotate.pack(side="left", padx=5)

        self.back_alarm_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_alarm = ctk.CTkButton(
            self.alarm_buttons_frame,
            image=self.back_alarm_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_alarm_command
            )
        self.Back_alarm.pack(side="left", padx=5)

    # ==========================================================
    # PROBE MENU
    # ==========================================================
        self.probe_frame = ctk.CTkFrame(self.frame, fg_color="transparent")

        self.probe_checkbox_frame= ctk.CTkFrame(self.probe_frame,
                                                width=100,
                                                fg_color="#b1b2b5",
                                                border_color="black",
                                                border_width=1,
                                                corner_radius=5)
        self.probe_checkbox_frame.pack(side="left")

        self.current_voltage=True

        def probe_current_checkbox_event():
            self.probe_voltage_checkbox.deselect()
            self.current_voltage=True

        check_var_current = ctk.BooleanVar(value=True)
        self.probe_current_checkbox = ctk.CTkCheckBox(self.probe_checkbox_frame, 
                                                text='Current', 
                                                command=probe_current_checkbox_event,
                                                width=40, 
                                                height=20, 
                                                checkbox_width=15, 
                                                checkbox_height=15,
                                                variable=check_var_current, 
                                                onvalue=True, 
                                                offvalue=False,
                                                border_width=1,
                                                border_color="black",
                                                text_color="black",
                                                font=(None, 20))
        self.probe_current_checkbox.pack(side="top", pady=1)

        def probe_voltage_checkbox_event():
            self.probe_current_checkbox.deselect()
            self.current_voltage=False
        
        check_var_voltage = ctk.BooleanVar(value=False)
        self.probe_voltage_checkbox = ctk.CTkCheckBox(self.probe_checkbox_frame, 
                                                text='Voltage', 
                                                command=probe_voltage_checkbox_event,
                                                width=40, 
                                                height=20, 
                                                checkbox_width=15, 
                                                checkbox_height=15,
                                                variable=check_var_voltage, 
                                                onvalue=True, 
                                                offvalue=False,
                                                border_width=1,
                                                border_color="black",
                                                text_color="black",
                                                font=(None, 20))
        self.probe_voltage_checkbox.pack(side="top", pady=1)

        self.probe_buttons_frame = ctk.CTkFrame(self.probe_frame, fg_color="transparent")
        self.probe_buttons_frame.pack(side="right", padx=15)

        self.probe_button_create_image = ctk.CTkImage(
            light_image=Image.open(PROBE_PATH),
            dark_image=Image.open(PROBE_PATH),
        )

        self.Probe_button_create = ctk.CTkButton(
            self.probe_buttons_frame,
            image=self.probe_button_create_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Probe_button_create.pack(side="left", padx=5)

        self.probe_button_create_image_rotate = ctk.CTkImage(
            light_image=Image.open(PROBE_PATH).rotate(90, expand=True),
            dark_image=Image.open(PROBE_PATH).rotate(90, expand=True),
        )

        self.Probe_button_create_rotate = ctk.CTkButton(
            self.probe_buttons_frame,
            image=self.probe_button_create_image_rotate,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5
            )
        self.Probe_button_create_rotate.pack(side="left", padx=5)

        self.back_probe_image = ctk.CTkImage(
            light_image=Image.open(BACK_PATH),
            dark_image=Image.open(BACK_PATH),
        )

        self.Back_probe = ctk.CTkButton(
            self.probe_buttons_frame,
            image=self.back_probe_image,
            text="",
            fg_color=botton_color,
            hover_color=botton_hover_color,
            border_color="black",
            border_width=1,
            corner_radius=5,
            command=self.back_probe_command
            )
        self.Back_probe.pack(side="left", padx=5)



    #we calculate the height of the toolbar
    def resize(self, event):
        new_height = max(70, int(self.root.winfo_height() / 8))
        button_size = int(new_height * 0.7)
        img_size = button_size - 10

        self.frame.configure(height=new_height)

    # --- Lista de todos los botones y sus imágenes ---
        items = [
            (self.Bee_button, self.bee_image),
            (self.Battery_button, self.battery_image),
            (self.Resistor_button, self.resistor_image),
            (self.Switch_button, self.switch_image),
            (self.Capacitor_button, self.capacitor_image),
            (self.Led_button, self.led_image),
            (self.Alarm_button, self.alarm_image),
            (self.Probe_button, self.probe_image),
            (self.Pause_play_button, self.pause_image),
            (self.Pause_play_button, self.play_image),

            (self.Battery_button_create, self.battery_button_create_image),
            (self.Battery_button_create_rotate, self.battery_button_create_image_rotate),
            (self.Back_battery, self.back_battery_image),

            (self.Resistor_button_create, self.resistor_button_create_image),
            (self.Resistor_button_create_rotate, self.resistor_button_create_image_rotate),
            (self.Back_resistor, self.back_resistor_image),

            (self.Switch_button_create, self.switch_button_create_image),
            (self.Switch_button_create_rotate, self.switch_button_create_image_rotate),
            (self.Back_switch, self.back_switch_image),

            (self.Capacitor_button_create, self.capacitor_button_create_image),
            (self.Capacitor_button_create_rotate, self.capacitor_button_create_image_rotate),
            (self.Back_capacitor, self.back_capacitor_image),

            (self.Led_button_create, self.led_button_create_image),
            (self.Led_button_create_rotate, self.led_button_create_image_rotate),
            (self.Back_led, self.back_led_image),

            (self.Alarm_button_create, self.alarm_button_create_image),
            (self.Alarm_button_create_rotate, self.alarm_button_create_image_rotate),
            (self.Back_alarm, self.back_alarm_image),

            (self.Probe_button_create, self.probe_button_create_image),
            (self.Probe_button_create_rotate, self.probe_button_create_image_rotate),
            (self.Back_probe, self.back_probe_image),
        ]

    # --- Asigna el tamaño dinámicamente ---
        for button, image in items:
            button.configure(height=button_size, width=button_size)
            image.configure(size=(img_size, img_size))

        # --- Otros frames dinámicos ---
        self.battery_creation_frame.configure(height=button_size)
        self.resistor_creation_frame.configure(height=button_size)
        self.capacitor_creation_frame.configure(height=button_size)
        self.capacitor_creation_frame_F.configure(height=button_size)
        self.alarm_checkbox_frame.configure(height=button_size)
        self.probe_checkbox_frame.configure(height=button_size)


    def main_battery_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.battery_frame.pack(side="left", padx=15)
    def back_battery_command(self):
        self.battery_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_resistor_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.resistor_frame.pack(side="left", padx=15)
    def back_resistor_command(self):
        self.resistor_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_switch_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.switch_frame.pack(side="left", padx=15)
    def back_switch_command(self):
        self.switch_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_capacitor_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.capacitor_frame.pack(side="left", padx=15)
    def back_capacitor_command(self):
        self.capacitor_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_led_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.led_frame.pack(side="left", padx=15)
    def back_led_command(self):
        self.led_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_alarm_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.alarm_frame.pack(side="left", padx=15)
    def back_alarm_command(self):
        self.alarm_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def main_probe_command(self):
        self.component_frame.pack_forget()
        self.other_frame.pack_forget()
        self.probe_frame.pack(side="left", padx=15)
    def back_probe_command(self):
        self.probe_frame.pack_forget()
        self.component_frame.pack(side="left", padx=10)
        self.other_frame.pack(side="left", padx=10)

    def set_controller(self, controller):
        self.controller = controller

    def main(self, button_name: str, parameter1, parameter2):
        print(f"{button_name} pressed with parameter1: {parameter1} and parameter2: {parameter2}")

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