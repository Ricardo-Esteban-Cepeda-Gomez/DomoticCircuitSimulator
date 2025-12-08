import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # src/
PROJECT_DIR = os.path.dirname(BASE_DIR)                # project/
DIST_DIR = os.path.join(PROJECT_DIR, "dist")
EXECUTABLE = os.path.join(DIST_DIR, "main")            # nombre normal de PyInstaller
ICON_PATH = os.path.join(BASE_DIR, "GUI", "images", "bee.png")

# Desktop entry path
DESKTOP_FILE = os.path.expanduser("~/.local/share/applications/beesmart.desktop")

desktop_entry = f"""[Desktop Entry]
Type=Application
Name=BeeSmart
Comment=Domotic Circuit Simulator
Exec={EXECUTABLE}
Icon={ICON_PATH}
Terminal=false
Categories=Utility;Development;
"""

# Create .desktop file
with open(DESKTOP_FILE, "w") as f:
    f.write(desktop_entry)

# Make it executable
os.chmod(DESKTOP_FILE, 0o755)

print("Archivo .desktop creado correctamente:")
print(DESKTOP_FILE)
