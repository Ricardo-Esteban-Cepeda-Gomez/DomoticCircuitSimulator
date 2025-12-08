import pickle
from workspace import Workspace

class FileManager:

    def save(self, ws: Workspace, path: str):
        with open(path, "wb") as f:
            pickle.dump(ws, f)
        print(f"Workspace '{ws.name}' guardado en {path}")

    def load(self, path: str) -> Workspace:
        with open(path, "rb") as f:
            ws = pickle.load(f)
        print(f"Workspace '{ws.name}' cargado desde {path}")
        return ws
