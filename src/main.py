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
from GUI.workspace_view import Workspace
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
    def __init__(self, root, resources, width=400, height=200):
        """
        Splash screen that updates progress while loading resources.
        
        Parameters:
        root (ctk.CTk): main window
        resources (list): list of functions that load resources
        """
        super().__init__(root)
        self.root = root
        self.resources = resources
        self.index = 0

        self.overrideredirect(True)
        self.width = width
        self.height = height

        # Center the splash screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.configure(fg_color="#1f1f1f")

        ctk.CTkLabel(
            self,
            text="BeeSmart Loading...",
            font=("Helvetica", 20),
            text_color="white"
        ).pack(pady=20)

        self.progress = ctk.CTkProgressBar(self, width=300)
        self.progress.pack(pady=40)
        self.progress.set(0)

        # Start loading resources
        self.after(100, self.load_next_resource)

    def load_next_resource(self):
        """Load resources sequentially and update progress bar"""
        if self.index < len(self.resources):
            # Call the next resource loader function
            self.resources[self.index]()
            self.index += 1

            # Update progress bar
            self.progress.set(self.index / len(self.resources))

            # Schedule next resource load
            self.after(50, self.load_next_resource)
        else:
            # All resources loaded, destroy splash
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
    global workspace
    workspace = Workspace(root)
    # Optional: add initial components
    workspace.add_component(50, 50)
    workspace.add_component(50, 50)

def load_statusbar():
    global statusbar
    statusbar = Statusbar(root)

# List of resource loader functions
resources = [load_menubar, load_toolbar, load_workspace, load_statusbar]

# ------------------------
# Show splash screen and load resources
# ------------------------
splash = SplashScreen(root, resources)
root.update()  # Force splash to show

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

# ------------------------
# Start main loop
# ------------------------
root.mainloop()