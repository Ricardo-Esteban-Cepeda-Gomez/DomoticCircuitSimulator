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
    @abstractmethod
    def burn(self):
        pass
    def fix_burn(self):
        self.is_burned = False
