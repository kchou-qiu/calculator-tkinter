import customtkinter as ctk
from typing import Callable


class KeypadButton(ctk.CTkButton):
    def __init__(self, parent: ctk.CTkFrame,
                 text: str = "",
                 command: Callable[..., None] = None,
                 row: int = 0,
                 column: int = 0,
                 columnspan: int = 0) -> None:
        super().__init__(parent, text=text, command=command)
        self.grid(row=row, column=column, columnspan=columnspan, sticky="NSEW")


class KeypadWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, max_rows: int, max_columns: int) -> None:
        super().__init__(parent)

        # grid layout
        for i in range(max_rows):
            self.rowconfigure(i, weight=1, uniform="a")

        for j in range(max_columns):
            self.columnconfigure(j, weight=1, uniform="a")
