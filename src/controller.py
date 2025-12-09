# controller.py
from logic.simulator import Simulator
from logic.file_manager import FileManager


class Controller:
    """
    Central controller that connects UI events with workspace actions.
    Routes toolbar commands, delegates simulation to Simulator,
    and updates both GUI and logic workspaces.
    """

    def __init__(self,root, gui_workspace, logic_workspace, toolbar=None, menubar=None, statusbar=None):
        # UI references
        self.root = root
        self.gui_workspace = gui_workspace
        self.toolbar = toolbar
        self.menubar = menubar
        self.statusbar = statusbar
        self.file_manager = FileManager(self.root)

        # Logic references
        self.logic_workspace = logic_workspace
        self.simulator = Simulator(self.logic_workspace)

        self.statusbar.set_simulator(self.simulator)

        # Bind modern toolbar event API
        if self.toolbar:
            self.toolbar.set_controller(self)

        # Bind global undo/redo shortcuts to controller (calls workspace methods)
        try:
            self.root.bind_all("<Control-z>", lambda e: self.undo())
            self.root.bind_all("<Control-y>", lambda e: self.redo())
            self.root.bind_all("<Control-o>", lambda e: self.load_workspace())
            self.root.bind_all("<Control-s>", lambda e: self.save_workspace())
        except Exception:
            pass
    # ================================================================
    # Undo / Redo wrappers (call Workspace methods)
    # ================================================================
    def undo(self):
        """Call the GUI workspace undo handler."""
        try:
            if hasattr(self.gui_workspace, "undo"):
                return self.gui_workspace.undo()
        except Exception as e:
            print(f"[Controller] undo failed: {e}")

    def redo(self):
        """Call the GUI workspace redo handler."""
        try:
            if hasattr(self.gui_workspace, "redo"):
                return self.gui_workspace.redo()
        except Exception as e:
            print(f"[Controller] redo failed: {e}")

    # ================================================================
    # Event Dispatcher (Toolbar → Controller)
    # ================================================================
    def on_toolbar_action(self, action_component: str, data, data2):
        """
        Central router for all toolbar actions.
        Allows toolbar to call controller without depending on internal methods.
        """
        print(f"[Controller] action='{action_component}', data={data}")
        # --- Simulation actions ----------------------------------------
        if action_component == "play":
            self.statusbar.update_status()
            return self.start_simulation()


        if action_component == "pause":
            self.statusbar.update_status()
            return self.stop_simulation()
            

        # --- Component creation actions --------------------------------
        # Normalize rotation suffix
        orientation = "horizontal"
        comp_name = action_component
        if action_component.endswith("_rotate"):
            comp_name = action_component.replace("_rotate", "")
            orientation = "vertical"

        # Data may be a dict or a scalar param
        params = {}
        if isinstance(data, dict):
            params.update(data)
        else:
            # common toolbar sends numeric params as data
            params["value"] = data

        # Default spawn position (could be enhanced to use mouse or center)
        spawn_x, spawn_y = 100, 100

        # Map toolbar names to component types used by GUI/logic
        mapping = {
            "battery": "source",
            "resistor": "resistor",
            "switch": "switch",
            "capacitor": "capacitor",
            "led": "led",
            "alarm": "alarm",
            "probe": "probe",
        }

        comp_type = mapping.get(comp_name.lower())
        if comp_type is None:
            print(f"[Controller] Unknown toolbar action: {action_component}")
            return

        # Ensure GUI workspace has reference to logic workspace
        try:
            self.gui_workspace.logic_workspace = self.logic_workspace
        except Exception:
            pass

        # Prepare creation kwargs depending on component type
        param_key_map = {
            "resistor": "resistance",
            "capacitor": "capacitance",
            "led": "color",
            "alarm": "frequency",
            "probe": "mode",
        }

        create_params = {}
        # if user passed explicit dict keys like 'resistance', use them
        if isinstance(data, dict):
            create_params.update(data)
        else:
            # numeric value -> map to expected kwarg if known
            val = data if data is not None else None
            key = param_key_map.get(comp_type)
            if key and val is not None:
                create_params[key] = val

        # Special-case Source (battery): create and then assign voltage
        try:
            group_id = self.gui_workspace.add_component(spawn_x, spawn_y, orientation, comp_type, component_params=create_params)
            if comp_type == "source":
                # if numeric value provided, set voltage on logical component
                logical = self.gui_workspace.component_map.get(group_id)
                if logical is not None:
                    if isinstance(params, dict) and "value" in params:
                        logical.voltage = params["value"]
                    elif not isinstance(params, dict) and params is not None:
                        logical.voltage = params
        except Exception as e:
            print(f"[Controller] Error creating component {comp_type}: {e}")

    # ================================================================
    # FileManager Logic
    # ================================================================

    def save_workspace(self):
        data = self.gui_workspace.serialize()
        self.file_manager.save(data)
    def load_workspace(self):
        data = self.file_manager.load()
        if data is None:
            return

        self.gui_workspace.load_from_data(data)


    # ================================================================
    # Simulation API
    # ================================================================
    def start_simulation(self):
        """Start continuous simulation."""
        self.simulator.start()

    def stop_simulation(self):
        """Pause simulation."""
        self.simulator.stop()

    def step_simulation(self):
        """Perform a single-step simulation."""
        self.simulator.step(force=True)

    # ================================================================
    # Called by main loop (root.after)
    # ================================================================
    def update(self):
        """Update simulation each frame."""
        self.simulator.step()  # Works only when simulator.running is True

    # ================================================================
    # Undo / Redo wrappers (call Workspace methods)
    # ================================================================
    def undo(self):
        """Call the GUI workspace undo handler."""
        try:
            if hasattr(self.gui_workspace, "undo"):
                return self.gui_workspace.undo()
        except Exception as e:
            print(f"[Controller] undo failed: {e}")

    def redo(self):
        """Call the GUI workspace redo handler."""
        try:
            if hasattr(self.gui_workspace, "redo"):
                return self.gui_workspace.redo()
        except Exception as e:
            print(f"[Controller] redo failed: {e}")