<<<<<<< Updated upstream
"""
Authors:
    Ricardo Esteban Cepeda Gomez
    Johan Sebastian Lievano Garcia
    Sebastian Vanegas
"""

import tkinter as tk
import platform
import customtkinter as ctk
import os
from PIL import Image, ImageTk
from GUI.menubar_view import Menubar
from GUI.toolbar_view import Toolbar
from GUI.workspace_view import Workspace as WorkspaceGUI
from logic.workspace import Workspace as WorkspaceLogic
from GUI.statusbar_view import Statusbar

ctk.set_default_color_theme("dark-blue")

# ------------------------
# Paths
# ------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "GUI", "images")
ICO_PATH = os.path.join(IMG_DIR, "bee.ico")
PNG_PATH = os.path.join(IMG_DIR, "bee.png")

# ------------------------
# Splash Screen Class
# ------------------------
class SplashScreen(ctk.CTkToplevel):
    def __init__(self, root, resources, icon_path, width=420, height=260, delay_per_step=250):
        """
        Splash screen with logo and controlled delay.

        Parameters:
            root            -> main window
            resources       -> list of functions to load
            icon_path       -> path to PNG logo
            delay_per_step  -> delay between resource loads (ms)
        """
        super().__init__(root)
        self.root = root
        self.resources = resources
        self.index = 0
        self.delay = delay_per_step

        # Hide the main window while splash loads
        self.root.withdraw()

        self.overrideredirect(True)

        # Center on screen
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.configure(fg_color="#1f1f1f")

        # -----------------------
        # Project Logo (PNG)
        # -----------------------
        self.logo = ctk.CTkImage(
            light_image=Image.open(icon_path),
            dark_image=Image.open(icon_path),
            size=(120, 120)
        )

        ctk.CTkLabel(self, image=self.logo, text="").pack(pady=(20, 10))

        # -----------------------
        # Title
        # -----------------------
        ctk.CTkLabel(
            self,
            text="BeeSmart is loading...",
            font=("Helvetica", 20),
            text_color="white"
        ).pack(pady=(0, 10))

        # Progress bar
        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=10)
        self.progress.set(0)

        # Start loading
        self.after(200, self.load_next_resource)

    def load_next_resource(self):
        if self.index < len(self.resources):

            # Load resource
            self.resources[self.index]()
            self.index += 1

            # Update progress
            self.progress.set(self.index / len(self.resources))

            # Delay to make splash slower
            self.after(self.delay, self.load_next_resource)

        else:
            # When all finished, show main window
            self.root.deiconify()
            self.destroy()


# ------------------------
# Main App
# ------------------------
root = ctk.CTk()
root.title("BeeSmart")
root.geometry("1200x700")
os_name = platform.system()

# Set icon
if os_name == "Windows":
    root.iconbitmap(ICO_PATH)
else:
    icon = tk.PhotoImage(file=PNG_PATH)
    root.iconphoto(True, icon)

# ------------------------
# Resource loading functions
# ------------------------
def load_menubar():
    global menu_bar
    menu_bar = Menubar(root)

def load_toolbar():
    global tool_bar
    tool_bar = Toolbar(root)

def load_workspace():
    global workspace, logic_workspace
    # Crear instancia lógica primero
    logic_workspace = WorkspaceLogic("main_workspace")
    # Crear instancia GUI pasando la lógica como parámetro
    workspace = WorkspaceGUI(root, logic_workspace)
    # Optional: add initial components
    workspace.add_component(100, 100, "horizontal", "source")
    workspace.add_component(250, 150, "vertical", "resistor")
    workspace.add_component(400, 200, "horizontal", "led")
    workspace.add_component(550, 250, "vertical", "alarm")
    workspace.add_component(250, 150, "vertical", "probe")
    workspace.add_component(400, 200, "horizontal", "probe")
    workspace.add_component(550, 250, "horizontal", "alarm")

def load_statusbar():
    global statusbar
    statusbar = Statusbar(root)

# ------------------------
# Resize handling for toolbar
# ------------------------
last_height = None

def on_resize(event):
    global last_height
    if last_height is None or abs(event.height - last_height) > 5:
        tool_bar.resize(event.height)
        last_height = event.height

root.bind("<Configure>", on_resize)

# List of resource loader functions
resources = [load_menubar, load_toolbar, load_workspace, load_statusbar]

# ------------------------
# Show splash screen and load resources
# ------------------------
splash = SplashScreen(root, resources, PNG_PATH, delay_per_step=500)
root.update()  # Force splash to show

# ------------------------
# Start main loop
# ------------------------
root.mainloop()
=======
>>>>>>> Stashed changes
