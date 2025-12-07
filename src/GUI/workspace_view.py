import tkinter as tk
import uuid

class Workspace():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="#ffffff")
        self.canvas.pack(side="top", fill="both", expand=True)

        # state
        self.drag_data = {"item": None, "x": 0, "y": 0, "current_group_tag": None}
        self.connection_data = {"start_port": None, "line": None}
        self.connections = []  # list

        # Events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def add_component(self, x=50, y=50, orientation="horizontal"):
        group_id = f"component_{uuid.uuid4().hex[:8]}"
        
        if orientation == "horizontal":
            w, h = 80, 40
            port_coords = [(x, y + h/2), (x + w, y + h/2)]
        else:
            w, h = 40, 80
            port_coords = [(x + w/2, y), (x + w/2, y + h)]

        # body
        self.canvas.create_rectangle(x, y, x+w, y+h, 
                                     fill="#4ea5ff", outline="black", 
                                     tags=(group_id, "body", "movable"))

        # Ports
        r = 5
        for px, py in port_coords:
            self.canvas.create_oval(px-r, py-r, px+r, py+r,
                                    fill="red", outline="black", width=1,
                                    tags=(group_id, "port"))

    def get_port_center(self, port_id):
        """returns port center given its id"""
        x1, y1, x2, y2 = self.canvas.coords(port_id)
        return ( (x1+x2)/2, (y1+y2)/2 )

    def on_click(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if items:
            top_item = items[-1]
            tags = self.canvas.gettags(top_item)

            # port
            if "port" in tags:
                if self.connection_data["start_port"] is None:
                    # Primer clic
                    self.connection_data["start_port"] = top_item
                    cx, cy = self.get_port_center(top_item)
                    self.connection_data["line"] = self.canvas.create_line(cx, cy, event.x, event.y, fill="black")
                else:
                    # Second click
                    start_port = self.connection_data["start_port"]
                    end_port = top_item
                    sx, sy = self.get_port_center(start_port)
                    ex, ey = self.get_port_center(end_port)
                    self.canvas.coords(self.connection_data["line"], sx, sy, ex, ey)
                    # save conection
                    self.connections.append((start_port, end_port, self.connection_data["line"]))
                    self.connection_data = {"start_port": None, "line": None}
                return

            # body
            if "body" in tags:
                group_tag = next((tag for tag in tags if tag.startswith("component_")), None)
                if group_tag:
                    self.drag_data["item"] = top_item
                    self.drag_data["current_group_tag"] = group_tag
                    self.drag_data["x"] = event.x
                    self.drag_data["y"] = event.y

    def on_drag(self, event):
        group_tag = self.drag_data["current_group_tag"]
        if group_tag:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(group_tag, dx, dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

            # update conections
            self.update_connections(group_tag)

        # cable
        if self.connection_data["start_port"] and self.connection_data["line"]:
            sx, sy = self.get_port_center(self.connection_data["start_port"])
            self.canvas.coords(self.connection_data["line"], sx, sy, event.x, event.y)

    def update_connections(self, group_tag):
        """recalculate pos"""
        for (p1, p2, line) in self.connections:
            tags1 = self.canvas.gettags(p1)
            tags2 = self.canvas.gettags(p2)
            if group_tag in tags1 or group_tag in tags2:
                x1, y1 = self.get_port_center(p1)
                x2, y2 = self.get_port_center(p2)
                self.canvas.coords(line, x1, y1, x2, y2)

    def on_release(self, event):
        self.drag_data = {"item": None, "x": 0, "y": 0, "current_group_tag": None}



