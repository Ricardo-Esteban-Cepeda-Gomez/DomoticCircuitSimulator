from collections import deque
from datetime import datetime
import logging
import threading
from typing import Callable, Deque, Dict, List, Any, Optional

from simulator import Simulator


class Statusbar:
    """
    Statusbar manejable para un simulador domótico.
    - Usa logging en lugar de prints.
    - Mantiene historial con timestamps.
    - Permite listeners (callbacks) para actualizar UI.
    - Es thread-safe.
    - Ahora registra y muestra la herramienta seleccionada (tool).
    """

    def __init__(self, sim: Simulator, max_history: int = 100, logger: logging.Logger | None = None):
        self.simulator = sim
        self.current_message: str = ""
        self.current_tool: Optional[str] = None
        self._history: Deque[Dict[str, str]] = deque(maxlen=max_history)
        self._lock = threading.RLock()
        self.logger = logger or logging.getLogger(__name__)
        self._listeners: List[Callable[[Dict[str, str]], None]] = []

    def _now(self) -> str:
        return datetime.utcnow().isoformat() + "Z"

    def _make_entry(self, message: str, level: int, tool: Optional[str]) -> Dict[str, str]:
        return {
            "time": self._now(),
            "message": message,
            "level": logging.getLevelName(level),
            "tool": tool or ""
        }

    def display_message(self, message: str, level: int = logging.INFO, tool: Optional[str] = None) -> None:
        """Muestra un mensaje (y lo registra en historial). Si se pasa 'tool', actualiza current_tool."""
        with self._lock:
            if tool is not None:
                self.current_tool = tool
            entry = self._make_entry(message, level, self.current_tool)
            self.current_message = message
            self._history.append(entry)
        # registrar con logging
        self.logger.log(level, "Status: %s (tool=%s)", message, self.current_tool)
        self._notify_listeners(entry)

    def set_tool(self, tool: Optional[str], level: int = logging.DEBUG) -> None:
        """Establece la herramienta seleccionada y registra la acción en el historial."""
        msg = f"Herramienta seleccionada: {tool}" if tool else "Herramienta deseleccionada"
        self.display_message(msg, level=level, tool=tool)

    def clear(self) -> None:
        """Borra el mensaje actual (registra la acción)."""
        self.display_message("", level=logging.DEBUG)

    def update(self, state: str) -> None:
        """Actualizar estado proveniente del simulador (API simple)."""
        self.display_message(f"Estado: {state}", level=logging.INFO)

    def update_from_simulator(self) -> None:
        """Extrae un estado simple del simulador si existe atributo 'state' y 'tool'."""
        state = getattr(self.simulator, "state", None)
        tool = getattr(self.simulator, "tool", None)
        # actualizar herramienta si existe
        if tool is not None:
            self.set_tool(str(tool))
        self.update(str(state))

    def add_listener(self, callback: Callable[[Dict[str, str]], None]) -> None:
        """Agregar un listener que recibe cada entrada de historial."""
        with self._lock:
            if callback not in self._listeners:
                self._listeners.append(callback)

    def remove_listener(self, callback: Callable[[Dict[str, str]], None]) -> None:
        with self._lock:
            if callback in self._listeners:
                self._listeners.remove(callback)

    def add_tk_listener(self, widget: Any, callback: Callable[[Dict[str, str]], None]) -> Callable[[Dict[str, str]], None]:
        """
        Añade un listener seguro para Tkinter.
        El callback original se ejecutará en el hilo de la UI usando widget.after(0, ...).
        Devuelve el wrapper agregado (útil para remove_listener).
        """
        def wrapper(entry: Dict[str, str]) -> None:
            try:
                # programar ejecución en el hilo principal de Tkinter
                widget.after(0, lambda: callback(entry))
            except Exception:
                self.logger.exception("Failed to schedule tkinter callback for entry: %s", entry)

        self.add_listener(wrapper)
        return wrapper

    def _notify_listeners(self, entry: Dict[str, str]) -> None:
        # notificar fuera del lock para evitar deadlocks en callbacks
        listeners: List[Callable[[Dict[str, str]], None]]
        with self._lock:
            listeners = list(self._listeners)
        for cb in listeners:
            try:
                cb(entry)
            except Exception:
                self.logger.exception("Listener falló al procesar entry: %s", entry)

    def get_history(self) -> List[Dict[str, str]]:
        """Devuelve una copia del historial (más reciente al final)."""
        with self._lock:
            return list(self._history)

    def get_current_tool(self) -> Optional[str]:
        with self._lock:
            return self.current_tool

    def __repr__(self) -> str:
        return f"<Statusbar current_message={self.current_message!r} current_tool={self.current_tool!r} history_len={len(self._history)}>"
