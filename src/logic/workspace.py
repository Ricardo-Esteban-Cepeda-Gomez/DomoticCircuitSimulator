from components.component import Component
from components.source import Source
from components.resistor import Resistor
from components.switch import Switch
from components.capacitor import Capacitor
from components.led import Led
from components.alarm import Alarm
from components.probes import Probes

class Workspace:
    def __init__(self, name=""):
        self.name = name
        self.components = []
        self.connections = []

    def add_component(self, Component):
        self.components = self.components + [Component]

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
        new_list = []
        for c in self.components:
            if c._component__id != componentId:
                new_list = new_list + [c]
        self.components = new_list

    def connect(self, comp1, comp2):
        self.connections = self.connections + [(comp1, comp2)]

    def disconnect(self, comp1, comp2):
        new_connections = []
        for c in self.connections:
            if c != (comp1, comp2):
                new_connections = new_connections + [c]
        self.connections = new_connections

    def simulate(self):
        print("Simulating workspace...")
