import tkinter as tk

class MenuBar:
    def __init__(self, root):
        self.root = root

        # Create custom menubar frame
        self.frame = tk.Frame(root, bg="#2d2d2d", height=28)
        self.frame.pack(fill="x", side="top")

        # Create menu items (File, Edit, View, Help)
        self.create_menu_button("File", ["New", "Open", "Save", "-", "Exit"])
        self.create_menu_button("Edit", ["Undo", "Redo"])
        self.create_menu_button("View", ["Zoom In", "Zoom Out"])
        self.create_menu_button("Help", ["About"])

    def create_menu_button(self, name, items):
        btn = tk.Label(self.frame, text=name, bg="#2d2d2d", fg="white", padx=10)
        btn.pack(side="left")

        # Dropdown menu
        menu = tk.Menu(self.root, tearoff=0)

        for item in items:
            if item == "-":
                menu.add_separator()
            elif item == "Exit":
                menu.add_command(label=item, command=self.root.quit)
            else:
                menu.add_command(label=item)

        # Show dropdown on click
        btn.bind("<Button-1>", lambda e, m=menu: self.show_menu(m, e))

    def show_menu(self, menu, event):
        menu.tk_popup(event.x_root, event.y_root)
