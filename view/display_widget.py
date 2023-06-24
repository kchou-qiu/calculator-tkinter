import customtkinter as ctk


class ResultsDisplayWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="OUTPUT", fg_color="#00ff00")
        self.label.pack(expand=True, fill="both")


class EquationDisplayWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="EQUATION", fg_color="#ff0000")
        self.label.pack(expand=True, fill="both")
