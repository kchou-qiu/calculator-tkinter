import customtkinter as ctk


class EquationWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.equation_label = ctk.CTkLabel(self, text="Equation", fg_color="#FF0000")
        self.equation_label.pack(expand=True, fill="both")
        self.grid(row=0, column=0, columnspan=4, sticky="SE")