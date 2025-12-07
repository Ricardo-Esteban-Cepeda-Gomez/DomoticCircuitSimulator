class Controller:
    def __init__(self, toolbar, workspace, properties, status):
        self.toolbar = toolbar
        self.workspace = workspace
        self.properties = properties
        self.status = status

        # Component buttons
        for name, btn in toolbar.buttons.items():
            btn.config(command=lambda n=name: self.select_component(n))

        toolbar.wire_btn.config(command=self.select_wire)
        toolbar.delete_btn.config(command=self.select_delete)

    def select_component(self, name):
        self.workspace.current_tool = "component"
        self.workspace.current_type = name
        self.status.update(f"Placing: {name}")

    def select_wire(self):
        self.workspace.current_tool = "wire"
        self.status.update("Wire tool selected")

    def select_delete(self):
        self.workspace.current_tool = "delete"
        self.status.update("Delete tool selected")