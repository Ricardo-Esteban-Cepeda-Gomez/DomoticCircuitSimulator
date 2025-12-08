import tkinter as tk
import uuid
import os
from PIL import Image, ImageTk

class Workspace():
    def __init__(self, root, logic_workspace=None):
        self.root = root
        self.logic_workspace = logic_workspace 
        self.canvas = tk.Canvas(root, bg="#ffffff")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.drag_data = {"item": None, "x": 0, "y": 0, "current_group_tag": None}
        self.connection_data = {"start_port": None, "line": None}
   
        self.connections = []

     
        self.port_map = {}          
        self.component_ports = {}    
     
        self.component_map = {}      

        base_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(base_dir, "images")

        self.sprites = {}
        for comp_type, filename in {
            "source": "battery.png",
            "resistor": "resistor.png",
            "switch": "switch.png",
            "capacitor": "capacitor.png",
            "led": "led.png",
            "alarm": "alarm.png",
            "probe": "probe.png"
        }.items():
            img_path = os.path.join(images_dir, filename)
            original = Image.open(img_path).resize((60, 60))
            rotated = original.rotate(90, expand=True)
            self.sprites[comp_type] = {
                "horizontal": ImageTk.PhotoImage(original),
                "vertical": ImageTk.PhotoImage(rotated)
            }

        # Eventos
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.root.bind("<Delete>", self.on_delete)

    def add_component(self, x=50, y=50, orientation="horizontal", comp_type="source"):
        group_id = f"component_{uuid.uuid4().hex[:8]}"

        w, h = 60, 60
        if orientation == "horizontal":
            port_coords = [(x - w//2, y), (x + w//2, y)]
        else:
            port_coords = [(x, y - h//2), (x, y + h//2)]

        sprite = self.sprites[comp_type][orientation]
        self.canvas.create_image(x, y, image=sprite,
                                 tags=(group_id, "body", "movable", orientation, comp_type))

 
        r = 5
        ports = []
        for idx, (px, py) in enumerate(port_coords):
            port_tag = f"port_{idx}"
            port_id = self.canvas.create_oval(px-r, py-r, px+r, py+r,
                                    fill="", outline="", width=0,
                                    tags=(group_id, "port", orientation, comp_type, port_tag))
            self.port_map[port_id] = (group_id, idx)
            ports.append(port_id)

        self.component_ports[group_id] = ports
        
  
        if self.logic_workspace is not None:
            try:
           
                component_params = {}
                
                if comp_type == "resistor":
                    component_params = {"resistance": 100.0, "max_power": 0.25}
                elif comp_type == "led":
                    component_params = {"color": "red", "max_current": 5.0}
                elif comp_type == "switch":
                    component_params = {"label": f"Switch_{group_id[:8]}"}
                elif comp_type == "capacitor":
                    component_params = {"capacitance": 1.0, "voltage_limit": 10.0}
                elif comp_type == "alarm":
                    component_params = {"volume": 50, "frequency": 440}
                elif comp_type == "probe":
                    component_params = {"mode": "voltage"}
          
                
              
                logical_component = self.logic_workspace.create_component(comp_type, **component_params)
                
                
                logical_component.position_x = x
                logical_component.position_y = y
                logical_component.rotation = 90 if orientation == "vertical" else 0
                
             
                self.component_map[group_id] = logical_component
                
                print(f"Componente lógico {comp_type} creado: {logical_component}")
            except Exception as e:
                print(f"Error al crear componente lógico {comp_type}: {e}")
        
        return group_id

    def get_orientation(self, item_id):
        tags = self.canvas.gettags(item_id)
        if "horizontal" in tags:
            return "horizontal"
        elif "vertical" in tags:
            return "vertical"
        return None

    def get_component_type(self, item_id):
        tags = self.canvas.gettags(item_id)
        for t in ["source", "resistor", "switch", "capacitor", "led", "alarm", "probe"]:
            if t in tags:
                return t
        return None

    def get_port_center(self, port_id):
        x1, y1, x2, y2 = self.canvas.coords(port_id)
        return ((x1+x2)/2, (y1+y2)/2)

    def on_click(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if not items:
            return

        top_item = items[-1]
        tags = self.canvas.gettags(top_item)

        if "port" in tags:
         
            if self.connection_data["start_port"] is None:
                self.connection_data["start_port"] = top_item
                cx, cy = self.get_port_center(top_item)
                self.connection_data["line"] = self.canvas.create_line(cx, cy, event.x, event.y, fill="black")
            else:
                start_port = self.connection_data["start_port"]
                end_port = top_item

             
                if start_port == end_port:
                 
                    self.canvas.delete(self.connection_data["line"])
                    self.connection_data = {"start_port": None, "line": None}
                    return

                c1 = self.port_map.get(start_port, (None, None))[0]
                c2 = self.port_map.get(end_port, (None, None))[0]
                if c1 is None or c2 is None:
                  
                    self.canvas.delete(self.connection_data["line"])
                    self.connection_data = {"start_port": None, "line": None}
                    return

                if c1 == c2:
                   
                    self.canvas.delete(self.connection_data["line"])
                    self.connection_data = {"start_port": None, "line": None}
                    return

               
                exists = False
                for conn in self.connections:
                    if (conn["p1"] == start_port and conn["p2"] == end_port) or \
                       (conn["p1"] == end_port and conn["p2"] == start_port):
                        exists = True
                        break
                if exists:
                    self.canvas.delete(self.connection_data["line"])
                    self.connection_data = {"start_port": None, "line": None}
                    return

                sx, sy = self.get_port_center(start_port)
                ex, ey = self.get_port_center(end_port)
                self.canvas.coords(self.connection_data["line"], sx, sy, ex, ey)

             
                conn_obj = {"p1": start_port, "p2": end_port, "line": self.connection_data["line"],
                            "c1": c1, "c2": c2}
                self.connections.append(conn_obj)

              
                self.canvas.itemconfigure(start_port, fill="black")
                self.canvas.itemconfigure(end_port, fill="black")

                self.connection_data = {"start_port": None, "line": None}
            return

        if "body" in tags:
            group_tag = next((tag for tag in tags if tag.startswith("component_")), None)
            if group_tag:
                self.drag_data["item"] = top_item
                self.drag_data["current_group_tag"] = group_tag
                self.drag_data["x"] = event.x
                self.drag_data["y"] = event.y

                orientation = self.get_orientation(top_item)
                comp_type = self.get_component_type(top_item)
                print(f"Este componente es {comp_type}, orientación {orientation}")

    def on_drag(self, event):
        group_tag = self.drag_data["current_group_tag"]
        if group_tag:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(group_tag, dx, dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
            self.update_connections(group_tag)

        if self.connection_data["start_port"] and self.connection_data["line"]:
            sx, sy = self.get_port_center(self.connection_data["start_port"])
            self.canvas.coords(self.connection_data["line"], sx, sy, event.x, event.y)

    def update_connections(self, group_tag):
        
        for conn in self.connections:
            p1 = conn["p1"]
            p2 = conn["p2"]
            tags1 = self.canvas.gettags(p1)
            tags2 = self.canvas.gettags(p2)
            if group_tag in tags1 or group_tag in tags2:
                x1, y1 = self.get_port_center(p1)
                x2, y2 = self.get_port_center(p2)
                self.canvas.coords(conn["line"], x1, y1, x2, y2)

    def on_release(self, event):
        self.drag_data = {"item": None, "x": 0, "y": 0, "current_group_tag": None}

    def on_delete(self, event):
        group_tag = self.drag_data["current_group_tag"]
        if group_tag:
            self.delete_component(group_tag)
            self.drag_data = {"item": None, "x": 0, "y": 0, "current_group_tag": None}

    def delete_component(self, group_tag):
        
        ports = self.component_ports.get(group_tag, [])
        to_remove = []
       
        for conn in list(self.connections):
            if conn["p1"] in ports or conn["p2"] in ports:
               
                try:
                    self.canvas.delete(conn["line"])
                except Exception:
                    pass
                
                other_port = conn["p2"] if conn["p1"] in ports else conn["p1"]
                
                if conn in self.connections:
                    self.connections.remove(conn)

               
                still_connected = any((c["p1"] == other_port or c["p2"] == other_port) for c in self.connections)
                if not still_connected:
                    try:
                        self.canvas.itemconfigure(other_port, fill="")
                    except Exception:
                        pass

      
        for p in ports:
            if p in self.port_map:
                del self.port_map[p]
        if group_tag in self.component_ports:
            del self.component_ports[group_tag]
        
       
        if group_tag in self.component_map:
            logical_component = self.component_map[group_tag]
            if self.logic_workspace is not None:
                self.logic_workspace.remove_component(logical_component._component__id)
            del self.component_map[group_tag]
            print(f"Componente lógico eliminado")

      
        self.canvas.delete(group_tag)


if __name__ == "__main__":
    root = tk.Tk()
    ws = Workspace(root)
    ws.add_component(100, 100, "horizontal", "source")
    ws.add_component(250, 150, "vertical", "resistor")
    ws.add_component(400, 200, "horizontal", "led")
    ws.add_component(550, 250, "vertical", "alarm")
    ws.add_component(700, 300, "horizontal", "probe")  
    root.mainloop()

