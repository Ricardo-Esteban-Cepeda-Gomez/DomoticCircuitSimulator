class component:
    def __init__(self):
        component.contador_id += 1
        self.__id = component.contador_id
        self.state = False
        self.positionX = 0.0
        self.positionY = 0.0
        self.rotation = 0
        self.inputs = []
        self.outputs = []
        self.isBurned = False
    def ConnectTo(self, component):
        pass
    def disconnect(self, component):
        pass
    def burn(self):
        self.isBurned = True
    def fixBurn(self):
        self.isBurned = False