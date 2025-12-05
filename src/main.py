""""
Authors:
    Ricardo Esteban Cepeda Gomez
    Johan Sebastian Lievano Garcia
    Sebastian Vanegas
"""
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from GUI.menubar_view import Menubar
from GUI.toolbar_view import Toolbar
from GUI.workspace_view import Workspace
from GUI.statusbar_view import Statusbar

ctk.set_default_color_theme("dark-blue")

#we create the main window
root = ctk.CTk()
root.title("BeeSmart")
root.geometry("1200x700")
root.overrideredirect(True)


#Menu bar created
menu_bar = Menubar(root)

#Tool bar created
tool_bar = Toolbar(root)

#Workspace canvas created
workspace = Workspace(root)

#Status bar creater
statusbar = Statusbar(root)

def on_resize(event):
    tool_bar.resize(event.height)

root.bind("<Configure>", on_resize)

#use the loop app
root.mainloop()
