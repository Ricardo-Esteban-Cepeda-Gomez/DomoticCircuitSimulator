import customtkinter as ctk
from PIL import Image

class Menubar:
    def __init__(self, root):
        self.root = root
        self.open_menu = None      # Stores the currently opened dropdown
        self.closing = False       # Prevents instant closing right after opening

        # Menubar frame
        self.frame = ctk.CTkFrame(root, height=35, fg_color="#ffffff", corner_radius=0)
        self.frame.pack(fill="x")
        self.frame.pack_propagate(False)

        # Font
        menubar_font = ctk.CTkFont("Source Code Pro", 20)

        # Bee icon
        bee_image = ctk.CTkImage(
            light_image=Image.open("src/GUI/images/bee.png"),
            dark_image=Image.open("src/GUI/images/bee.png"),
            size=(21, 21)
        )
        self.bee_label = ctk.CTkLabel(self.frame, image=bee_image, text="")
        self.bee_label.pack(side="left")

        # File button
        self.filebutton = ctk.CTkButton(
            self.frame,
            text="File",
            width=60,
            fg_color="#ffffff",
            text_color="black",
            hover_color="#dcdcdc",
            corner_radius=5,
            font=menubar_font,
            command=self.toggle_filemenu
        )
        self.filebutton.pack(side="left")

    # ---------------------------------
    # OPEN / CLOSE LOGIC
    # ---------------------------------
    def toggle_filemenu(self):
        """Opens the menu if closed, closes it if already open."""
        if self.closing:
            return

        if self.open_menu:
            self.close_menu()
            return

        self.show_filemenu()

    def show_filemenu(self):
        """Creates and displays the dropdown menu under the File button."""
        # Get button position relative to its parent frame
        bx = self.filebutton.winfo_rootx() - self.frame.winfo_rootx()
        by = self.filebutton.winfo_rooty() - self.frame.winfo_rooty()

        # Menu container
        menu = ctk.CTkFrame(self.root, fg_color="#e6e6e6", corner_radius=5)
        menu.place(x=bx, y=by + self.filebutton.winfo_height())
        menu.lift()

        self.open_menu = menu

        # Dropdown options
        for text in ("New", "Open", "Save"):
            ctk.CTkButton(
                menu,
                text=text,
                width=120,
                fg_color="#e6e6e6",
                text_color="black",
                hover_color="#c5c5c5",
            ).pack(padx=5, pady=3)

        # Enable close-on-hover only AFTER the user can enter the menu
        self.root.after(150, lambda: self.enable_close_events(menu))

    def enable_close_events(self, menu):
        """Allows the menu to close when mouse leaves both menu and button."""
        menu.bind("<Leave>", lambda e: self.start_menu_close())
        self.filebutton.bind("<Leave>", lambda e: self.start_menu_close())

    def start_menu_close(self):
        """Triggers the closing logic with delay to prevent accidental closing."""
        if not self.open_menu:
            return

        self.closing = True
        self.root.after(120, self.check_close)

    def check_close(self):
        """Closes the menu only if the mouse is NOT over menu nor button."""
        if not self.open_menu:
            self.closing = False
            return

        # Mouse position
        x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()

        over_menu = self.is_inside(self.open_menu, x, y)
        over_btn  = self.is_inside(self.filebutton, x, y)

        if not over_menu and not over_btn:
            self.close_menu()

        self.closing = False

    def is_inside(self, widget, px, py):
        """Checks if a point (mouse) is inside a widget."""
        wx = widget.winfo_rootx()
        wy = widget.winfo_rooty()
        ww = widget.winfo_width()
        wh = widget.winfo_height()

        return wx <= px <= wx + ww and wy <= py <= wy + wh

    def close_menu(self):
        """Hides the dropdown menu."""
        if self.open_menu:
            self.open_menu.place_forget()
            self.open_menu = None