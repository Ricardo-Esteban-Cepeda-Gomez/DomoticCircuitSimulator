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
        """Adds a component instance to the logical workspace."""
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
            raise ValueError(f"Invalid component type: {comp_type}")
        

        component = ComponentClass(**kwargs)
        

        self.add_component(component)
        
        return component

    def remove_component(self, componentId):
        # Allows receiving instance or id
        target_id = componentId.id if hasattr(componentId, "id") else componentId
        new_list = [c for c in self.components if not (hasattr(c, "id") and c.id == target_id)]
        self.components = new_list
        # also remove connections that involve this id
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
        """Connects two components indicating the port index in each one.
        comp1/comp2 can be instances or ids.
        Connections stored as (a_id, a_port, b_id, b_port).
        """
        id1 = comp1.id if hasattr(comp1, "id") else comp1
        id2 = comp2.id if hasattr(comp2, "id") else comp2
        if id1 == id2:
            return
        pair = (id1, int(port1_index), id2, int(port2_index))
        # avoid duplicates (regardless of order and port)
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
        # DEBUG: quick summary at the beginning
        try:
            print(f"[Workspace] update dt={dt} components={len(self.components)} connections={len(self.connections)}")
            print(f"[Workspace] connections: {self.connections}")
        except Exception:
            pass

        # Map id -> instance
        comp_map = {c.id: c for c in self.components}

        # adjacency list
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
            # BFS/DFS to get all nodes of the subgraph
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

            # get instances of the subgraph
            comps = [comp_map[i] for i in sub_ids if i in comp_map]

            # DEBUG: show detected subgraph
            try:
                print(f"[Workspace] subgraph nodes={sub_ids}")
            except Exception:
                pass

            # detect sources in the subgraph
            sources = [c for c in comps if isinstance(c, Source)]

            if len(sources) == 0:
                # Without source, set currents to 0 and call local updates if they exist
                for c in comps:
                    c.input_current = 0.0
                    c.output_current = 0.0
                    # try to call update methods if available
                    try:
                        if hasattr(c, "update_state"):
                            # some update_state accept parameters, others do not
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

            # if there is more than one source, use the first and log (no crash)
            source = sources[0]
            V = getattr(source, "voltage", 0.0)

            # calculate total resistance in the subgraph (sum of resistors)
            resistors = [c for c in comps if isinstance(c, Resistor)]
            total_R = sum(getattr(r, "resistance", 0.0) for r in resistors)
            if total_R <= 0.0:
                # safe fallback to avoid division by zero
                total_R = 1.0

            # series current (approx): I = V / R_total
            I = V / total_R

            # DEBUG: show source and calculated current
            try:
                print(f"[Workspace] source_id={source.id} V={V} total_R={total_R} I={I}")
            except Exception:
                pass

            # assign current to the source
            try:
                source.current = I
                source.output_current = I
            except Exception:
                pass

            # update resistors (we pass them the expected voltage drop)
            for r in resistors:
                try:
                    Vr = I * getattr(r, "resistance", 0.0)
                    # Resistor.update_state waits for input_voltage
                    r.update_state(Vr)
                except Exception:
                    # try calling
                    try:
                        r.update_state()
                    except Exception:
                        pass

            # LEDs: apply input current and update
            leds = [c for c in comps if isinstance(c, Led)]
            for led in leds:
                try:
                    led.input_current = I
                    # some leds use update_state()
                    if hasattr(led, "update_state"):
                        try:
                            led.update_state()
                        except TypeError:
                            led.update_state(I)
                except Exception:
                    pass

            # Capacitors
            caps = [c for c in comps if isinstance(c, Capacitor)]
            for cap in caps:
                try:
                    cap.input_current = I
                    if hasattr(cap, "update"):
                        cap.update()
                except Exception:
                    pass

            # Alarms: on if theres current
            alarms = [c for c in comps if isinstance(c, Alarm)]
            for a in alarms:
                try:
                    if I > 0 and not a.is_on:
                        a.turn_on()
                    elif I <= 0 and a.is_on:
                        a.turn_off()
                except Exception:
                    pass

            # Probes: connect and measure the first component (e.g. the source)
            probes = [c for c in comps if isinstance(c, Probes)]
            for p in probes:
                try:
                    p.connect()
                    p.measure(source)
                except Exception:
                    pass

    def simulate(self):
        # simple wrapper for compatibility 
        try:
            self.update(1.0)
        except Exception:
            pass
