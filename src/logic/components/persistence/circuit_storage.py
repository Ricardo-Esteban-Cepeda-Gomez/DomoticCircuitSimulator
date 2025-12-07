import json
from classes.snippets.component import Component

class CircuitStorage:

    @staticmethod
    def save(circuit, file_path: str):
        data = {
            "components": [
                {
                    "type": component.__class__.__name__,
                    "attributes": component.__dict__
                }
                for component in circuit
            ]
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load(file_path: str):
        from classes.snippets.component import Component

        with open(file_path, "r") as file:
            data = json.load(file)

        loaded_components = []

        for comp_data in data["components"]:
            class_name = comp_data["type"]
            attributes = comp_data["attributes"]

            module = __import__("classes.snippets." + class_name.lower(), fromlist=[class_name])
            cls = getattr(module, class_name)

            obj = cls.__new__(cls)
            obj.__dict__.update(attributes)

            loaded_components.append(obj)

        return loaded_components