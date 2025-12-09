import pickle
from tkinter import filedialog, messagebox
import os


class FileManager:
    def __init__(self, root):
        self.root = root

    # ----------------------------------------------------
    # SAVE WORKSPACE
    # ----------------------------------------------------
    def save(self, workspace, path: str = None):
        """
        Save a workspace to a file.

        Args:
            workspace: Dictionary with 'components' and 'connections' structure
            path: File path (if None, opens a save dialog)
        """

        try:
            # Ask for a path if not provided
            if path is None:
                path = filedialog.asksaveasfilename(
                    title="Save Workspace",
                    defaultextension=".bsm",
                    filetypes=[("BeeSmart File", "*.bsm"), ("All Files", "*.*")]
                )

                if not path:
                    return  # User canceled

            # Validate workspace is serializable
            if not isinstance(workspace, dict):
                raise ValueError("The workspace must be a dictionary with 'components' and 'connections' structure")
            
            if "components" not in workspace or "connections" not in workspace:
                raise ValueError("The workspace must contain 'components' and 'connections'")

            # Try to serialize before saving
            test_pickle = pickle.dumps(workspace)

            # Save the file
            with open(path, "wb") as f:
                f.write(test_pickle)

            messagebox.showinfo("Success", f"Workspace saved to:\n{path}")
            print(f"✓ Workspace saved to: {path}")

            # Update main window title with saved filename
            try:
                self.root.title(f"BeeSmart - {os.path.basename(path)}")
            except Exception:
                pass

        except Exception as e:
            error_msg = f"Error saving: {str(e)}"
            messagebox.showerror("Save Error", error_msg)
            print(f"✗ {error_msg}")

    # ----------------------------------------------------
    # LOAD WORKSPACE
    # ----------------------------------------------------
    def load(self):
        """
        Load a workspace from a file.

        Returns:
            Dictionary with 'components' and 'connections' structure, or None on error
        """
        try:
            path = filedialog.askopenfilename(
                title="Load Workspace",
                filetypes=[("BeeSmart File", "*.bsm"), ("All Files", "*.*")]
            )

            if not path:
                return None  # User canceled

            # Validate that the file exists
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file does not exist: {path}")

            # Validate file size (should not be empty)
            if os.path.getsize(path) == 0:
                raise EOFError("The file is empty.")

            # Load the file
            with open(path, "rb") as f:
                data = pickle.load(f)

            # Validate structure of loaded file
            if not isinstance(data, dict):
                raise ValueError("The file does not contain a valid workspace (must be a dictionary)")

            if "components" not in data or "connections" not in data:
                raise ValueError("The file does not have the expected structure (missing 'components' or 'connections')")

            messagebox.showinfo("Success", f"Workspace loaded from:\n{path}")
            print(f"✓ Workspace loaded from: {path}")

            # Update main window title with loaded filename
            try:
                self.root.title(f"BeeSmart - {os.path.basename(path)}")
            except Exception:
                pass
            return data

        except FileNotFoundError as e:
            error_msg = f"File not found: {str(e)}"
            messagebox.showerror("Load Error", error_msg)
            print(f"✗ {error_msg}")
            return None

        except EOFError:
            error_msg = "The file is empty or corrupt."
            messagebox.showerror("Load Error", error_msg)
            print(f"✗ {error_msg}")
            return None

        except pickle.UnpicklingError as e:
            error_msg = f"The file is corrupt: {str(e)}"
            messagebox.showerror("Load Error", error_msg)
            print(f"✗ {error_msg}")
            return None

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            messagebox.showerror("Load Error", error_msg)
            print(f"✗ {error_msg}")
            return None