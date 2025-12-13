from logic.components.component import Component
from logic.components.source import Source
from logic.components.resistor import Resistor
from logic.components.switch import Switch
from logic.components.capacitor import Capacitor
from logic.components.led import Led
from logic.components.alarm import Alarm
from logic.components.probes import Probes

class Workspace:
    def __init__(self, name=""):
        self.name = name
        self.components = []
        self.connections = []

    def add_component(self, component):
        """Añade una instancia de componente al workspace lógico."""
        self.components = self.components + [component]

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
        # Permite recibir instancia o id
        target_id = componentId.id if hasattr(componentId, "id") else componentId
        new_list = [c for c in self.components if not (hasattr(c, "id") and c.id == target_id)]
        self.components = new_list
        # también eliminar conexiones que involucren a este id
        self.connections = [conn for conn in self.connections if conn[0] != target_id and conn[1] != target_id]

    def connect(self, comp1, comp2):
        """Conecta dos componentes. `comp1`/`comp2` pueden ser instancias o ids."""
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        if id1 == id2:
            return
        pair = (id1, id2)
        # evitar duplicados (independientemente del orden)
        if any((c == pair or c == (pair[1], pair[0])) for c in self.connections):
            return
        self.connections = self.connections + [pair]

    def disconnect(self, comp1, comp2):
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        self.connections = [c for c in self.connections if not (c == (id1, id2) or c == (id2, id1))]

    def update(self, dt: float = 1.0):
        """logic network updates based on ohms law
        """
        # DEBUG: resumen rápido al inicio
        try:
            print(f"[Workspace] update dt={dt} components={len(self.components)} connections={len(self.connections)}")
            print(f"[Workspace] connections: {self.connections}")
        except Exception:
            pass

        # Mapa id -> instancia
        comp_map = {c.id: c for c in self.components}

        # construir lista de adyacencia
        adj = {c.id: set() for c in self.components}
        for a, b in list(self.connections):
            if a in adj and b in adj:
                adj[a].add(b)
                adj[b].add(a)

        visited = set()
        for cid in list(adj.keys()):
            if cid in visited:
                continue
            # BFS/DFS para obtener todos los nodos del subgrafo
            stack = [cid]
            sub_ids = []
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                sub_ids.append(cur)
                for nb in adj.get(cur, ()):  # neighbors
                    if nb not in visited:
                        stack.append(nb)

            # obtener instancias del subgrafo
            comps = [comp_map[i] for i in sub_ids if i in comp_map]

            # DEBUG: mostrar subgrafo detectado
            try:
                print(f"[Workspace] subgraph nodes={sub_ids}")
            except Exception:
                pass

            # detectar fuentes en el subgrafo
            sources = [c for c in comps if isinstance(c, Source)]

            if len(sources) == 0:
                # Sin fuente, poner corrientes a 0 y llamar a updates locales si existen
                for c in comps:
                    c.input_current = 0.0
                    c.output_current = 0.0
                    # intentar llamar a métodos de actualización if available
                    try:
                        if hasattr(c, "update_state"):
                            # algunos update_state aceptan parámetros, otros no
                            try:
                                c.update_state(0.0)
                            except TypeError:
                                c.update_state()
                    except Exception:
                        pass
                    try:
                        if hasattr(c, "update"):
                            c.update()
                    except Exception:
                        pass
                continue

            # si hay más de una fuente, usar la primera y loggear (no crash)
            source = sources[0]
            V = getattr(source, "voltage", 0.0)

            # calcular resistencia total en el subgrafo (suma de resistores)
            resistors = [c for c in comps if isinstance(c, Resistor)]
            total_R = sum(getattr(r, "resistance", 0.0) for r in resistors)
            if total_R <= 0.0:
                # fallback seguro para evitar división por cero
                total_R = 1.0

            # corriente en serie (aprox): I = V / R_total
            I = V / total_R

            # DEBUG: mostrar fuente y corriente calculada
            try:
                print(f"[Workspace] source_id={source.id} V={V} total_R={total_R} I={I}")
            except Exception:
                pass

            # asignar corriente a la fuente
            try:
                source.current = I
                source.output_current = I
            except Exception:
                pass

            # actualizar resistores (les pasamos la caída de tensión esperada)
            for r in resistors:
                try:
                    Vr = I * getattr(r, "resistance", 0.0)
                    # Resistor.update_state espera input_voltage
                    r.update_state(Vr)
                except Exception:
                    # intentar llamada sin args si firma difiere
                    try:
                        r.update_state()
                    except Exception:
                        pass

            # LEDs: aplicar corriente entrante y actualizar
            leds = [c for c in comps if isinstance(c, Led)]
            for led in leds:
                try:
                    led.input_current = I
                    # algunos leds usan update_state()
                    if hasattr(led, "update_state"):
                        try:
                            led.update_state()
                        except TypeError:
                            led.update_state(I)
                except Exception:
                    pass

            # Capacitores: pasar corriente de carga y actualizar
            caps = [c for c in comps if isinstance(c, Capacitor)]
            for cap in caps:
                try:
                    cap.input_current = I
                    if hasattr(cap, "update"):
                        cap.update()
                except Exception:
                    pass

            # Alarms: encender si hay corriente
            alarms = [c for c in comps if isinstance(c, Alarm)]
            for a in alarms:
                try:
                    if I > 0 and not a.is_on:
                        a.turn_on()
                    elif I <= 0 and a.is_on:
                        a.turn_off()
                except Exception:
                    pass

            # Probes: conectar y medir la primera componente (ej. la fuente)
            probes = [c for c in comps if isinstance(c, Probes)]
            for p in probes:
                try:
                    p.connect()
                    p.measure(source)
                except Exception:
                    pass

    def simulate(self):
        # simple wrapper para compatibilidad: actualiza con paso por defecto
        try:
            self.update(1.0)
        except Exception:
            pass
