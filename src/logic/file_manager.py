import pickle
from tkinter import filedialog
from workspace import Workspace

class FileManager:

    def save(self, ws: Workspace, path: str = None):
        if path is None:
            path = filedialog.asksaveasfilename(
                defaultextension=".pkl",
                filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")]
            )
            if not path:  # User cancelled
                return
        
        with open(path, "wb") as f:
            pickle.dump(ws, f)
        print(f"Workspace '{ws.name}' guardado en {path}")

    def load(self, path: str = None) -> Workspace:
        if path is None:
            path = filedialog.askopenfilename(
                filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")]
            )
            if not path:  # User cancelled
                return None
        
        with open(path, "rb") as f:
            ws = pickle.load(f)
        print(f"Workspace '{ws.name}' cargado desde {path}")
        return ws
