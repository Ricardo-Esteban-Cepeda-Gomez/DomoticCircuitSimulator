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
from PIL import Image
from GUI.menubar_view import Menubar
from GUI.toolbar_view import Toolbar
from GUI.workspace_view import Workspace
from GUI.statusbar_view import Statusbar
from controller import Controller

ctk.set_default_color_theme("dark-blue")

# ------------------------
# Paths
# ------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "GUI", "images")
ICO_PATH = os.path.join(IMG_DIR, "bee.ico")
PNG_PATH = os.path.join(IMG_DIR, "bee.png")

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
# COMPONENT CREATION (ORDER MATTERS)
# ------------------------

# 1) Workspace (GUI canvas)
workspace = Workspace(root)

# 2) Controller (logic)
controller = Controller()
controller.set_workspace(workspace)

# 3) Toolbar (needs controller)
tool_bar = Toolbar(root)
tool_bar.set_controller(controller)

# 4) Menubar
menu_bar = Menubar(root)

# 5) Statusbar
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


# ------------------------
# Start App
# ------------------------
root.mainloop()