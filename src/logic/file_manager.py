import pickle
from tkinter import filedialog, messagebox


class FileManager:
    def __init__(self):
        pass

    # ----------------------------------------------------
    # SAVE WORKSPACE
    # ----------------------------------------------------
    def save(self, workspace, path: str = None):
        try:
            # Ask for path if none
            if path is None:
                path = filedialog.asksaveasfilename(
                    title="Save Workspace",
                    defaultextension=".wrk",
                    filetypes=[("Workspace File", "*.wrk"), ("All Files", "*.*")]
                )

                if not path:
                    return  # user cancelled

            with open(path, "wb") as f:
                pickle.dump(workspace, f)

            print(f"Workspace saved to {path}")

        except Exception as e:
            messagebox.showerror("Save Error", str(e))
            print("Error saving workspace:", e)

    # ----------------------------------------------------
    # LOAD WORKSPACE
    # ----------------------------------------------------
    def load(self):
        try:
            path = filedialog.askopenfilename(
                title="Load Workspace",
                filetypes=[("Workspace File", "*.wrk"), ("All Files", "*.*")]
            )

            if not path:
                return None  # user cancelled

            with open(path, "rb") as f:
                data = pickle.load(f)

            print(f"Workspace loaded from {path}")
            return data  # Could be workspace object or dict

        except EOFError:
            messagebox.showerror("Load Error", "The file is empty or corrupted.")
            print("Error: EOFError (empty/corrupt file)")
            return None

        except Exception as e:
            messagebox.showerror("Load Error", str(e))
            print("Error loading workspace:", e)
            return None