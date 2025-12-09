@echo off
REM Build Windows .exe using PyInstaller. Run this on Windows in a command prompt.
REM Usage: open an Administrator command prompt in the repo root and run build_windows.bat

REM 1) Install dependencies (recommended in a virtualenv)
python -m pip install -r requirements.txt

REM 2) Create one-file windowed executable (change icon path if you want)
REM --add-data syntax for Windows uses semicolon between src and dest
pyinstaller --noconfirm --clean --onefile --windowed --name BeeSmart \
  --icon "src/GUI/images/bee.ico" \
  --add-data "src/GUI/images;GUI/images" \
  src/main.py

if %ERRORLEVEL% EQU 0 (
  echo Build succeeded. Find output in the dist\BeeSmart.exe or dist\BeeSmart folder.
) else (
  echo Build failed with errorlevel %ERRORLEVEL%.
)

pause
