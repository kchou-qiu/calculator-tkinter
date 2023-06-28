import customtkinter as ctk


class DisplayWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, anchor: str, font: ctk.CTkFont) -> None:
        super().__init__(parent)
        self._display = ctk.StringVar(self)
        self.label = ctk.CTkLabel(self, textvariable=self._display, font=font, anchor=anchor)
        self.label.pack(expand=True, fill="both")

    def update_display(self, equation: str) -> None:
        self._display.set(equation)
