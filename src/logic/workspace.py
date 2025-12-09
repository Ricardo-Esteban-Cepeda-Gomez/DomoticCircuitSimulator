from logic.components.component import Component
from logic.components.source import Source
from logic.components.resistor import Resistor
from logic.components.switch import Switch
from logic.components.capacitor import Capacitor
from logic.components.led import Led
from logic.components.alarm import Alarm
from logic.components.probes import Probes

class Workspace:
    def __init__(self, name=""):
        self.name = name
        self.components = []
        self.connections = []

    def add_component(self, component):
        """Añade una instancia de componente al workspace lógico."""
        self.components = self.components + [component]

    def create_component(self, comp_type, **kwargs):

        component_map = {
            "source": Source,
            "resistor": Resistor,
            "switch": Switch,
            "capacitor": Capacitor,
            "led": Led,
            "alarm": Alarm,
            "probe": Probes
        }
        
        ComponentClass = component_map.get(comp_type)
        if ComponentClass is None:
            raise ValueError(f"Tipo de componente no válido: {comp_type}")
        

        component = ComponentClass(**kwargs)
        

        self.add_component(component)
        
        return component

    def remove_component(self, componentId):
        # Permite recibir instancia o id
        target_id = componentId.id if hasattr(componentId, "id") else componentId
        new_list = [c for c in self.components if not (hasattr(c, "id") and c.id == target_id)]
        self.components = new_list
        # también eliminar conexiones que involucren a este id
        self.connections = [conn for conn in self.connections if conn[0] != target_id and conn[1] != target_id]

    def connect(self, comp1, comp2):
        """Conecta dos componentes. `comp1`/`comp2` pueden ser instancias o ids."""
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        if id1 == id2:
            return
        pair = (id1, id2)
        # evitar duplicados (independientemente del orden)
        if any((c == pair or c == (pair[1], pair[0])) for c in self.connections):
            return
        self.connections = self.connections + [pair]

    def disconnect(self, comp1, comp2):
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        self.connections = [c for c in self.connections if not (c == (id1, id2) or c == (id2, id1))]

    def simulate(self):
        print("Simulating workspace...")
