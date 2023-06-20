import customtkinter as ctk


class KeypadWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.keypad = ctk.CTkLabel(self, text="Keypad", fg_color="#00FF00")
        self.keypad.pack(expand=True, fill="both")
        self.grid(row=2, column=0, rowspan=5, columnspan=4, sticky="NSEW")