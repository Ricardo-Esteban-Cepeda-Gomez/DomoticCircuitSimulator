class Cable:
    contador_id = 0

    def __init__(self, port_a, port_b):
        Cable.contador_id += 1
        self.id = Cable.contador_id
        self.port_a = port_a
        self.port_b = port_b

       
        port_a.connect(self)
        port_b.connect(self)

    def disconnect(self):
        self.port_a.disconnect()
        self.port_b.disconnect()
