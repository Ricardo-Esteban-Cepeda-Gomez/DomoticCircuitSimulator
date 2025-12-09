# controller.py
from logic.simulator import Simulator

class Controller:
    """
    Central controller that connects UI events with workspace actions.
    It routes toolbar commands, delegates simulation to Simulator,
    and updates the workspace.
    """

    def __init__(self, workspace, toolbar=None, menubar=None, statusbar=None):
        # UI references
        self.workspace = workspace
        self.toolbar = toolbar
        self.menubar = menubar
        self.statusbar = statusbar

        # Logic references
        self.simulator = Simulator(self.workspace)

        # Bind toolbar button callbacks (optional legacy compatibility)
        if self.toolbar:
            self.toolbar.on_sim_start = self.start_simulation
            self.toolbar.on_sim_stop = self.stop_simulation
            self.toolbar.on_sim_step = self.step_simulation

        # Bind modern toolbar event API
        if self.toolbar:
            self.toolbar.set_controller(self)

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
            return self.start_simulation()

        if action_component == "pause":
            return self.stop_simulation()

        # --- Workspace actions -----------------------------------------
        if action_component == "battery":
            value = data.get("value", 0.0)
            return self.workspace.add_component(100, 100, "horizontal", f"battery:{value}")

        if action_component == "delete_selected":
            return self.workspace.delete_selected()

        # Unknown action fallback
        print(f"[Controller] Unknown toolbar action: {action_component}")

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