import customtkinter as ctk
from PIL import Image
import os

class Menubar:
    def __init__(self, root):
        self.root = root
        self.open_menu = None
        self.closing = False

        # Top menubar container
        self.frame = ctk.CTkFrame(root, height=35, fg_color="#ffffff", corner_radius=0)
        self.frame.pack(fill="x")
        self.frame.pack_propagate(False)

        # Font
        self.menubar_font = ctk.CTkFont("Source Code Pro", 20)

        # Bee icon
        # Absolute path to the directory of this file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        IMG_DIR = os.path.join(BASE_DIR, "images")

        # Icon paths
        PNG_PATH = os.path.join(IMG_DIR, "bee.png")

        bee_image = ctk.CTkImage(
            light_image=Image.open(PNG_PATH),
            dark_image=Image.open(PNG_PATH),
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
            font=self.menubar_font,
            command=self.toggle_filemenu
        )
        self.filebutton.pack(side="left")

        # Edit button
        self.editbutton = ctk.CTkButton(
            self.frame,
            text="Edit",
            width=60,
            fg_color="#ffffff",
            text_color="black",
            hover_color="#dcdcdc",
            corner_radius=5,
            font=self.menubar_font,
            command=self.toggle_editmenu
        )
        self.editbutton.pack(side="left")

        # Help button
        self.helpbutton = ctk.CTkButton(
            self.frame,
            text="Help",
            width=60,
            fg_color="#ffffff",
            text_color="black",
            hover_color="#dcdcdc",
            corner_radius=5,
            font=self.menubar_font,
            command=self.toggle_helpmenu
        )
        self.helpbutton.pack(side="left")


    # ==========================================================
    # GENERIC MENU OPEN/CLOSE HANDLING
    # ==========================================================

    def toggle_filemenu(self):
        """Toggles the File menu open/close"""
        if self.closing:
            return

        if self.open_menu:
            self.close_menu()
        else:
            self.show_filemenu()

    def toggle_editmenu(self):
        """Toggles the Edit menu open/close"""
        if self.closing:
            return

        if self.open_menu:
            self.close_menu()
        else:
            self.show_editmenu()

    def toggle_helpmenu(self):
        """Toggles the Help menu open/close"""
        if self.closing:
            return

        if self.open_menu:
            self.close_menu()
        else:
            self.show_helpmenu()

    # ==========================================================
    # FILE MENU
    # ==========================================================

    def show_filemenu(self):
        bx = self.filebutton.winfo_rootx() - self.frame.winfo_rootx()
        by = self.filebutton.winfo_rooty() - self.frame.winfo_rooty()

        menu = self.create_menu(bx, by + self.filebutton.winfo_height())

        for text in ("New (Ctrl+N)", "Open (Ctrl+O)", "Save (Ctrl+S)"):
            self.create_menu_item(menu, text)

        self.enable_close_after_delay(menu, self.filebutton)

    # ==========================================================
    # EDIT MENU
    # ==========================================================

    def show_editmenu(self):
        bx = self.editbutton.winfo_rootx() - self.frame.winfo_rootx()
        by = self.editbutton.winfo_rooty() - self.frame.winfo_rooty()

        menu = self.create_menu(bx, by + self.editbutton.winfo_height())

        for text in ("Undo (Ctrl+Z)", "Redo (Ctrl+Y)"):
            self.create_menu_item(menu, text)

        self.enable_close_after_delay(menu, self.editbutton)

    # ==========================================================
    # HELP MENU  (THIS WAS BROKEN BEFORE — NOW FIXED)
    # ==========================================================

    def show_helpmenu(self):
        bx = self.helpbutton.winfo_rootx() - self.frame.winfo_rootx()
        by = self.helpbutton.winfo_rooty() - self.frame.winfo_rooty()

        menu = self.create_menu(bx, by + self.helpbutton.winfo_height())

        self.create_menu_item(menu, "About")

        self.enable_close_after_delay(menu, self.helpbutton)

    # ==========================================================
    # MENU BUILDING HELPERS
    # ==========================================================

    def create_menu(self, x, y):
        """Creates and places a floating menu frame"""
        menu = ctk.CTkFrame(self.root, fg_color="#e6e6e6", corner_radius=5, bg_color="transparent")
        menu.place(x=x, y=y)
        menu.lift()
        self.open_menu = menu
        return menu

    def create_menu_item(self, menu, text):
        """Creates a button inside a menu"""
        ctk.CTkButton(
            menu,
            text=text,
            width=140,
            fg_color="#e6e6e6",
            text_color="black",
            hover_color="#c5c5c5",
            anchor="w",
            corner_radius=5
        ).pack(padx=5, pady=3)

    # ==========================================================
    # MENU AUTO-CLOSE LOGIC
    # ==========================================================

    def enable_close_after_delay(self, menu, button):
        """Wait before enabling hover-close to avoid instant closing"""
        self.root.after(200, lambda: self.enable_close_events(menu, button))

    def enable_close_events(self, menu, button):
        """Adds reliable hover-close behavior."""

        # Remove old bindings from previous menus
        menu.unbind("<Leave>")
        menu.unbind("<Enter>")

        button.unbind("<Leave>")
        button.unbind("<Enter>")

        # Bind menu leave → check if mouse REALLY left the menu
        menu.bind("<Leave>", lambda e, m=menu, b=button: self.handle_menu_leave(e, m, b))

        # If user enters the menu again → cancel closing
        menu.bind("<Enter>", lambda e: self.cancel_close())

        # Button interactions
        button.bind("<Leave>", lambda e, m=menu, b=button: self.start_menu_close(m, b))
        button.bind("<Enter>", lambda e: self.cancel_close())


    def handle_menu_leave(self, event, menu, button):
        """Triggered by <Leave> but checks if user really left the menu."""

        x, y = event.x_root, event.y_root

        # Menu bounding box
        mx1 = menu.winfo_rootx()
        my1 = menu.winfo_rooty()
        mx2 = mx1 + menu.winfo_width()
        my2 = my1 + menu.winfo_height()

        # If mouse still inside → ignore fake <Leave>
        if mx1 <= x <= mx2 and my1 <= y <= my2:
            return

        self.start_menu_close(menu, button)



    def is_inside_any(self, widgets, px, py):
        for widget in widgets:
            if self.is_inside(widget, px, py):
                return True
        return False

    def start_menu_close(self, menu, button):
        """Starts the delayed close process."""
        self.closing = True
        self.root.after(120, lambda m=menu, b=button: self.check_close(m, b))


    def cancel_close(self):
        """Cancels a pending close."""
        self.closing = False


    def check_close(self, menu, button):
        if not self.closing:
            return

        px, py = self.root.winfo_pointerx(), self.root.winfo_pointery()

        # Menu still hovered → don't close
        if self.is_inside(menu, px, py):
            self.closing = False
            return

        # Button still hovered → don't close
        if self.is_inside(button, px, py):
            self.closing = False
            return

        # Close it
        self.close_menu()
        self.closing = False

    def is_inside(self, widget, px, py):
        """Checks if mouse is inside a widget"""
        wx, wy = widget.winfo_rootx(), widget.winfo_rooty()
        ww, wh = widget.winfo_width(), widget.winfo_height()
        return wx <= px <= wx + ww and wy <= py <= wy + wh

    def close_menu(self):
        """Hides and resets the menu"""
        if self.open_menu:
            self.open_menu.place_forget()
            self.open_menu = None
