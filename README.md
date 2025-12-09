# Domotic Circuit Simulator — BeeSmart

### Universidad Nacional de Colombia  
**Object-Oriented Programming — Eng. Carlos Andrés Sierra Virgüez**  
**Authors:** Ricardo Esteban Cepeda Gómez, Johan Sebastian Liévano García, Sebastián Vanegas Ariza  
**Date:** December 09, 2025

---

## User Guide — Quick start

This section gives a concise, app-oriented walkthrough so a new user can open the app and build a working circuit in minutes.

Requirements
- Python 3.10 or newer
- Recommended: a virtual environment

Install dependencies (from project root):

```bash
python -m pip install -r requirements.txt
```

Run the app:

```bash
python src/main.py
```

Main window layout
- Menubar: File / Edit / Help and quick access to Save/Open/Undo/Redo actions
- Toolbar: drag or click component icons to add them to the workspace
- Workspace: central canvas where you place components, draw wires and move items
- Statusbar: shows simulation state and quick messages

Keyboard shortcuts
- Ctrl+S — Save project
- Ctrl+O — Open project
- Ctrl+Z — Undo
- Ctrl+Y — Redo
- F1     — Open the documentation
- Delete — Delete selected component

File format
- Workspaces are saved as binary workspace files (default extension `.wrk`). The File Manager uses Python `pickle` to serialize the workspace dictionary.

---

## Practical Usage Example

1. Start the app (`python src/main.py`).
2. From the toolbar add a `Source` (battery), `Switch`, and an `LED`.
3. Click on component ports to draw a wire connecting Source → Switch → LED.
4. Click Start in the statusbar to run the simulation and observe the LED lighting up when the switch is closed.
5. Use File → Save to store the workspace; the filename appears in the window title.

---

## Features (what this app does)

- Visual circuit building with drag & drop components
- Connect components via clickable port wiring
- Basic simulation loop: components update each frame
- Save / Load workspace files
- Undo / Redo support (Ctrl+Z / Ctrl+Y)
- Simple component set: Source, Resistor, LED, Switch, Capacitor, Alarm, Probe

---

## Developer Notes (project structure)

Top-level source layout (inside `src/`):

- `GUI/` — Tkinter / customtkinter views (menubar, toolbar, workspace, statusbar)
- `logic/` — core simulation, components, file manager and workspace logic
- `controller.py` — application controller glue between GUI and logic
- `main.py` — application entry point

File highlights
- `logic/file_manager.py` — handles saving/loading workspaces (.wrk)
- `src/GUI/workspace_view.py` — canvas rendering, user interactions, undo/redo support
- `logic/components/` — component implementations (LED, Alarm, Resistor, etc.)

Development tips
- The workspace keeps a serializable dict via `serialize()` and `load_from_data()` to restore state.
- Undo/Redo uses in-memory snapshots of `serialize()`; adjust `push_undo()` calls in `workspace_view.py` if you want different granularity.

---

## Troubleshooting & Known limitations

- Audio for the Alarm component requires `simpleaudio` (optional). If not installed the app will log a message instead of playing sound.
- Saved files use `pickle` — do not open .wrk files from untrusted sources.
- Some UI polish and advanced component parameter editing are work-in-progress.

---

## Contributing

Contributions are welcome. Please open issues or PRs on the GitHub repository. Keep changes small and add tests where appropriate.

---

## Team / Credits

- Authors: Ricardo Esteban Cepeda Gómez, Johan Sebastian Liévano García, Sebastián Vanegas Ariza
- Professor: Eng. Carlos Andrés Sierra Virgüez
- Universidad: Universidad Nacional de Colombia

---

*End of file*