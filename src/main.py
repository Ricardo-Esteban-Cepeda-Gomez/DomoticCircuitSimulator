import tkinter as tk
import platform
import customtkinter as ctk
import os
from PIL import Image

from GUI.menubar_view import Menubar
from GUI.toolbar_view import Toolbar
from GUI.workspace_view import Workspace as GUIWorkspace
from logic.workspace import Workspace as LogicWorkspace
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
# Main Window
# ------------------------
root = ctk.CTk()
root.title("BeeSmart - UnsavedFile")
root.geometry("1200x700")


# ------------------------
# Window Icon
# ------------------------
if platform.system() == "Windows":
    root.iconbitmap(ICO_PATH)
else:
    root.iconphoto(True, tk.PhotoImage(file=PNG_PATH))


# ================================================================
# GUI CREATION ORDER (visual stacking)
# 1. Menubar     (top)
# 2. Toolbar     (under the menubar)
# 3. Workspace   (center)
# 4. Statusbar   (bottom)
# ================================================================

menu_bar = Menubar(root)          # Top menu bar
tool_bar = Toolbar(root)          # Toolbar
# Create logical workspace and pass it to the view for synchronization
logic_workspace = LogicWorkspace()
workspace = GUIWorkspace(root, logic_workspace=logic_workspace)       # Main drawing/work area (GUI)
statusbar = Statusbar(root, )       # Bottom bar


# ================================================================
# Controller Setup (logic layer)
# ================================================================

# Controller receives the workspace and toolbar directly
controller = Controller(
    root = root,
    gui_workspace=workspace,
    logic_workspace=logic_workspace,
    toolbar=tool_bar,
    menubar=menu_bar,
    statusbar=statusbar
)

# Toolbar connects back to controller (for event dispatch)
tool_bar.set_controller(controller)
menu_bar.set_controller(controller)

# Menubar can also receive controller if needed
# menu_bar.set_controller(controller)


# ================================================================
# Resize Handling (Toolbar Responsiveness)
# ================================================================
last_height = None

def on_resize(event):
    """Resize toolbar only when height changes significantly."""
    global last_height
    if last_height is None or abs(event.height - last_height) > 5:
        tool_bar.resize(event.height)
        last_height = event.height

root.bind("<Configure>", on_resize)


# ================================================================
# Update Loop (Simulation + Workspace)
# ================================================================
def update_loop():
    controller.update()      # Runs simulator step
    root.after(16, update_loop)  # ~60 FPS

update_loop()


# ------------------------
# Start Application
# ------------------------
root.mainloop()
