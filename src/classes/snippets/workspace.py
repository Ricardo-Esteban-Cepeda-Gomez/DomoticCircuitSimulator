from Component import component

class workspace:
    def __init__(self, name=""):
        self.name = name
        self.components = []
        self.connections = []

    def addComponent(self, component):
        self.components = self.components + [component]

    def removeComponent(self, componentId):
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
