from workspace import workspace

class Filemanager:
    def save(self, ws: workspace, path: str):
        print(f"Saving workspace '{ws.name}' to {path}")

    def load(self, path: str):
        print(f"Loading workspace from {path}")
        return workspace("LoadedWorkspace")
