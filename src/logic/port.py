class Port:
    contador_id = 0

    def __init__(self, parent_component, is_input=False):
        Port.contador_id += 1
        self.id = Port.contador_id
        self.parent = parent_component   
        self.is_input = is_input
        self.connected_cable = None
        self.logical_network_id = None   
        self.state = False               
        self.voltage = 0.0               
        self.current = 0.0               

    def connect(self, cable):
        self.connected_cable = cable

    def disconnect(self):
        self.connected_cable = None
