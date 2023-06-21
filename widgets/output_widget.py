import customtkinter as ctk


class OutputWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="OUTPUT", fg_color="#00ff00")
        self.label.pack(expand=True, fill="both")
