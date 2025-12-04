from workspace import Workspace

class Filemanager:
    def save(self, ws: Workspace, path: str):
        print(f"Saving workspace '{ws.name}' to {path}")

    def load(self, path: str):
        print(f"Loading workspace from {path}")
        return Workspace("LoadedWorkspace")
