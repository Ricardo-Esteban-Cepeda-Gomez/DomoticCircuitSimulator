import pickle
from tkinter import filedialog, messagebox
import os


class FileManager:
    def __init__(self):
        pass

    # ----------------------------------------------------
    # SAVE WORKSPACE
    # ----------------------------------------------------
    def save(self, workspace, path: str = None):
        """
        Guarda un workspace en un archivo.
        
        Args:
            workspace: Diccionario con estructura de componentes y conexiones
            path: Ruta del archivo (si es None, abre diálogo de guardado)
        """
        try:
            # Pedir ruta si no se proporciona
            if path is None:
                path = filedialog.asksaveasfilename(
                    title="Guardar Workspace",
                    defaultextension=".wrk",
                    filetypes=[("Archivo de Workspace", "*.wrk"), ("Todos los Archivos", "*.*")]
                )

                if not path:
                    return  # Usuario canceló

            # Validar que el workspace sea serializable
            if not isinstance(workspace, dict):
                raise ValueError("El workspace debe ser un diccionario con estructura 'components' y 'connections'")
            
            if "components" not in workspace or "connections" not in workspace:
                raise ValueError("El workspace debe contener 'components' y 'connections'")

            # Intentar serializar antes de guardar
            test_pickle = pickle.dumps(workspace)

            # Guardar el archivo
            with open(path, "wb") as f:
                f.write(test_pickle)

            messagebox.showinfo("Éxito", f"Workspace guardado en:\n{path}")
            print(f"✓ Workspace guardado en: {path}")

        except Exception as e:
            error_msg = f"Error al guardar: {str(e)}"
            messagebox.showerror("Error de Guardado", error_msg)
            print(f"✗ {error_msg}")

    # ----------------------------------------------------
    # LOAD WORKSPACE
    # ----------------------------------------------------
    def load(self):
        """
        Carga un workspace desde un archivo.
        
        Returns:
            Diccionario con estructura de componentes y conexiones, o None si hay error
        """
        try:
            path = filedialog.askopenfilename(
                title="Cargar Workspace",
                filetypes=[("Archivo de Workspace", "*.wrk"), ("Todos los Archivos", "*.*")]
            )

            if not path:
                return None  # Usuario canceló

            # Validar que el archivo existe
            if not os.path.exists(path):
                raise FileNotFoundError(f"El archivo no existe: {path}")

            # Validar tamaño del archivo (no debe estar vacío)
            if os.path.getsize(path) == 0:
                raise EOFError("El archivo está vacío.")

            # Cargar el archivo
            with open(path, "rb") as f:
                data = pickle.load(f)

            # Validar estructura del archivo cargado
            if not isinstance(data, dict):
                raise ValueError("El archivo no contiene un workspace válido (debe ser diccionario)")
            
            if "components" not in data or "connections" not in data:
                raise ValueError("El archivo no tiene la estructura esperada (falta 'components' o 'connections')")

            messagebox.showinfo("Éxito", f"Workspace cargado desde:\n{path}")
            print(f"✓ Workspace cargado desde: {path}")
            return data

        except FileNotFoundError as e:
            error_msg = f"Archivo no encontrado: {str(e)}"
            messagebox.showerror("Error de Carga", error_msg)
            print(f"✗ {error_msg}")
            return None

        except EOFError:
            error_msg = "El archivo está vacío o corrupto."
            messagebox.showerror("Error de Carga", error_msg)
            print(f"✗ {error_msg}")
            return None

        except pickle.UnpicklingError as e:
            error_msg = f"El archivo está corrupto: {str(e)}"
            messagebox.showerror("Error de Carga", error_msg)
            print(f"✗ {error_msg}")
            return None

        except Exception as e:
            error_msg = f"Error inesperado: {str(e)}"
            messagebox.showerror("Error de Carga", error_msg)
            print(f"✗ {error_msg}")
            return None