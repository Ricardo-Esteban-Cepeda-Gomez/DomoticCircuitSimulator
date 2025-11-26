from abc import ABC, abstractmethod
class Component(ABC):
    contador_id = 0

    def __init__(self):
        Component.contador_id += 1
        
        self.__id = Component.contador_id
        self.state = False
        self.position_x = 0.0
        self.position_y = 0.0
        self.rotation = 0
        self.is_burned = False
        self.input_current = 0.0
        self.output_current = 0.0
    def burn(self):
        self.is_burned = True
    def fix_burn(self):
        self.is_burned = False
