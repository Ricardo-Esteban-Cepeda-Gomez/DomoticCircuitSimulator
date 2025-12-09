import logging
from typing import Optional

from logic.workspace import Workspace

class Simulator:
    """Simple simulator for the Workspace. Uses logging instead of prints,
    validates dt, integrates with Workspace.update(dt) if present,
    and exposes start/stop/step methods."""
    def __init__(self, ws: Workspace, dt_default: float = 1.0):
        # Reference to the Workspace where circuit components are stored
        self.workspace = ws

        self.time = 0.0
        self.dt_default = dt_default

        self.running = True

        self.logger = logging.getLogger(__name__)

    def start(self):
        self.running = True
        self.logger.info("Simulation started")

    def stop(self):
        self.running = False
        self.logger.info("Simulation stopped")

    def toggle(self):
        self.running = not self.running
        self.logger.info(f"Simulation running: {self.running}")

    def update(self, dt: float):
        """Call workspace update (if implemented) and perform any per-step logic."""
        # If workspace implements update(dt), call it. Otherwise do nothing.
        try:
            update_fn = getattr(self.workspace, "update", None)
            if callable(update_fn):
                update_fn(dt)
                self.logger.debug("Workspace updated")
            else:
                self.logger.debug("Workspace has no update(dt) method")
        except Exception as exc:
            self.logger.exception("Error while updating workspace: %s", exc)

    def step(self, dt: Optional[float] = None, force: bool = False):
        """Advance simulation by dt.
        If force is True, step even when simulation is stopped (useful for single-step).
        """
        if dt is None:
            dt = self.dt_default

        if dt <= 0:
            self.logger.warning("Ignored step with non-positive dt: %s", dt)
            return

        if not self.running and not force:
            self.logger.debug("Simulation paused - step ignored")
            return

        self.time += dt
        self.logger.debug("Simulation time: %s", self.time)
        self.update(dt)
# ...existing code...
