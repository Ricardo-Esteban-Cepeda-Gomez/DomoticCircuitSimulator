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
    @property
    def id(self):
        """ID público (lectura) del componente."""
        return self.__id

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} pos=({self.position_x},{self.position_y}) rot={self.rotation}>"
