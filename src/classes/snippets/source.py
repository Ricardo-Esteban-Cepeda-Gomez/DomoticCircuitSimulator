from Component import component

class Source(component):

    def __init__(self):
        self.__type = "AC"
        self.current = 0.0
        self.voltage = 0.0