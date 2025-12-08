#!/bin/bash

echo "🐝 Building BeeSmart..."

# Always detect project root automatically
PROJECT_DIR="$(dirname "$(realpath "$0")")"

SRC_DIR="$PROJECT_DIR/src"
IMG_DIR="$SRC_DIR/GUI/images"

DIST_DIR="$SRC_DIR/dist"
APP_DIR="$HOME/BeeSmart"

MAIN_FILE="$SRC_DIR/main.py"

# Check for main.py
if [ ! -f "$MAIN_FILE" ]; then
    echo "❌ ERROR: main.py not found at: $MAIN_FILE"
    exit 1
fi

echo "📦 Compiling with PyInstaller..."
pyinstaller "$MAIN_FILE" \
    --noconsole \
    --onefile \
    --add-data "$IMG_DIR:GUI/images" \
    --icon="$IMG_DIR/icon.ico"

echo "📂 Creating app directory at $APP_DIR..."
mkdir -p "$APP_DIR"

# Check dist output
if [ ! -f "$DIST_DIR/main" ]; then
    echo "❌ ERROR: Executable not found at: $DIST_DIR/main"
    exit 1
fi

echo "📁 Copying executable..."
cp "$DIST_DIR/main" "$APP_DIR/BeeSmart"

echo "🖼 Copying images folder..."
mkdir -p "$APP_DIR/GUI/images"
cp -r "$IMG_DIR/"* "$APP_DIR/GUI/images/"

echo "📝 Creating .desktop file..."

DESKTOP_FILE="$HOME/.local/share/applications/beesmart.desktop"

cat <<EOF > "$DESKTOP_FILE"
[Desktop Entry]
Version=1.0
Type=Application
Name=BeeSmart
Comment=Domotic Circuit Simulator
Exec=$APP_DIR/BeeSmart
Icon=$APP_DIR/GUI/images/icon.ico
Terminal=false
Categories=Utility;Education;
EOF

echo "🔄 Updating desktop database..."
update-desktop-database ~/.local/share/applications/ 2>/dev/null || true

chmod +x "$DESKTOP_FILE"
chmod +x "$APP_DIR/BeeSmart"

echo "✅ Installation complete!"
echo "🐝 BeeSmart is now available in your applications menu."