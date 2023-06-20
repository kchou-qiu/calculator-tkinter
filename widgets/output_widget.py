import customtkinter as ctk


class OutputWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.output = ctk.CTkLabel(self, text="Results", fg_color="#0000FF")
        self.output.pack(expand=True, fill="both")
        self.grid(row=1, column=0, columnspan=4, sticky="E")
