""""
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

# Absolute path to the directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "GUI", "images")

# Icon paths
ICO_PATH = os.path.join(IMG_DIR, "bee.ico")
PNG_PATH = os.path.join(IMG_DIR, "bee.png")

#we create the main window
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


#Menu bar created
menu_bar = Menubar(root)

#Tool bar created
tool_bar = Toolbar(root)

#Workspace canvas created
workspace = Workspace(root)

workspace.add_component(50, 50)
workspace.add_component(50, 50)

#Status bar creater
statusbar = Statusbar(root)

def on_resize(event):
    tool_bar.resize(event.height)

root.bind("<Configure>", on_resize)

#use the loop app
root.mainloop()
