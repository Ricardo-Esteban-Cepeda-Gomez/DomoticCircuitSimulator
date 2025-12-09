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
# Main Application Window
# ------------------------
root = ctk.CTk()
root.title("BeeSmart")
root.geometry("1200x700")

# ------------------------
# Set Application Icon
# ------------------------
if platform.system() == "Windows":
    root.iconbitmap(ICO_PATH)
else:
    icon = tk.PhotoImage(file=PNG_PATH)
    root.iconphoto(True, icon)

# ================================================================
# GUI CREATION ORDER (visual stacking)
# 1. Menubar     (top)
# 2. Toolbar     (under the menubar)
# 3. Workspace   (center area)
# 4. Statusbar   (bottom)
# ================================================================

# Create GUI components in the required visual order
menu_bar = Menubar(root)          # Top menu bar
tool_bar = Toolbar(root)          # Toolbar below the menubar
workspace = Workspace(root)       # Main workspace area
statusbar = Statusbar(root)       # Bottom status bar

# ================================================================
# Controller setup (logic layer)
# The controller is initialized after GUI components but does not
# affect their visual order. It only links their interaction.
# ================================================================
controller = Controller()

# Connect controller with workspace (logic → view)
controller.set_workspace(workspace)

# Connect controller with toolbar (view → logic)
tool_bar.set_controller(controller)

# If needed later:
# menu_bar.set_controller(controller)

# ------------------------
# Resize handling for toolbar
# ------------------------
last_height = None

def on_resize(event):
    """
    Resizes the toolbar only when the window height
    changes significantly to avoid performance issues.
    """
    global last_height
    if last_height is None or abs(event.height - last_height) > 5:
        tool_bar.resize(event.height)
        last_height = event.height

root.bind("<Configure>", on_resize)

# ------------------------
# Start main loop
# ------------------------
root.mainloop()