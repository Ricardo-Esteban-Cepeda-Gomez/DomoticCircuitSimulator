import pickle

class FileManager:

    def save(self, ws: workspace, path: str):
        with open(path, "wb") as f:
            pickle.dump(workspace, f)
        print(f"Workspace '{workspace.name}' guardado en {path}")

    def load(self, path: str) -> workspace:
        with open(path, "rb") as f:
            workspace = pickle.load(f)
        print(f"Workspace '{workspace.name}' cargado desde {path}")
        return workspace
