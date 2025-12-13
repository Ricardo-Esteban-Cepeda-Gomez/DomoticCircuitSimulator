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
        # connections are stored as tuples: (a_id, a_port, b_id, b_port)
        self.connections = [conn for conn in self.connections if conn[0] != target_id and conn[2] != target_id]

    def connect(self, comp1, comp2):
        """Deprecated signature. Use connect(comp1, port1_index, comp2, port2_index).
        Backwards-compatible: if called with two args, assume a generic undirected connection using port indices (0,0).
        """
        # Backwards compatibility: allow connect(comp1, comp2) but prefer explicit ports
        if not (hasattr(comp1, 'id') and (not isinstance(comp2, int) and not hasattr(comp2, 'id')) ):
            pass
        # If caller provided 4 args (handled by caller), this function will be overridden by kwargs.
        raise TypeError("connect requires signature connect(comp1, port1_index, comp2, port2_index)")
    
    def connect_with_ports(self, comp1, port1_index, comp2, port2_index):
        """Conecta dos componentes indicando el índice de puerto en cada uno.
        comp1/comp2 pueden ser instancias o ids.
        Connections stored as (a_id, a_port, b_id, b_port).
        """
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        if id1 == id2:
            return
        pair = (id1, int(port1_index), id2, int(port2_index))
        # evitar duplicados (independientemente del orden y de puerto)
        for c in self.connections:
            if c == pair or c == (pair[2], pair[3], pair[0], pair[1]):
                return
        self.connections.append(pair)

    def disconnect(self, comp1, comp2):
        raise TypeError("disconnect requires signature disconnect(comp1, port1_index, comp2, port2_index)")
    
    def disconnect_with_ports(self, comp1, port1_index, comp2, port2_index):
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        pair = (id1, int(port1_index), id2, int(port2_index))
        pair_rev = (id2, int(port2_index), id1, int(port1_index))
        self.connections = [c for c in self.connections if c != pair and c != pair_rev]

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
        # adjacency now respects port directionality. connections items are (a_id,a_port,b_id,b_port)
        adj = {c.id: set() for c in self.components}
        for a_id, a_port, b_id, b_port in list(self.connections):
            if a_id in adj and b_id in adj:
                ca = comp_map.get(a_id)
                cb = comp_map.get(b_id)
                # helper to decide if current can flow from owner -> other through the given port
                def allows_edge(owner, owner_port):
                    try:
                        # Switch: only allows if closed
                        if isinstance(owner, Switch):
                            return owner.allows_current()
                        # Led: allow only from port 1 (anode) outward
                        if hasattr(owner, '__class__') and owner.__class__.__name__ == 'Led':
                            return int(owner_port) == 1
                        # Source: allow only from port 1 (positive)
                        if isinstance(owner, Source):
                            return int(owner_port) == 1
                        # Other components: bidirectional
                        return True
                    except Exception:
                        return True

                try:
                    if allows_edge(ca, a_port) and (not (isinstance(cb, Switch) and not cb.allows_current())):
                        adj[a_id].add(b_id)
                    if allows_edge(cb, b_port) and (not (isinstance(ca, Switch) and not ca.allows_current())):
                        adj[b_id].add(a_id)
                except Exception:
                    pass

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
