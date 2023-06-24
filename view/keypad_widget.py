import customtkinter as ctk
from typing import Callable
from assets.config import *


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
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(parent)

        self.equation = ""
        self.numbers = []

        # grid layout
        for i in range(KEY_ROWS):
            self.rowconfigure(i, weight=1, uniform="a")

        for j in range(KEY_COLS):
            self.columnconfigure(j, weight=1, uniform="a")

        for number, data in NUMBER_BUTTONS.items():
            KeypadButton(self,
                         text=str(number),
                         command=lambda: self.number_press(number),
                         row=data["row"], column=data["column"],
                         columnspan=data["columnspan"])

        for operator, data in OPERATOR_BUTTONS.items():
            KeypadButton(self, row=data["row"], column=data["column"], columnspan=data["columnspan"])

        for special, data in SPECIAL_BUTTONS.items():
            KeypadButton(self, row=data["row"], column=data["column"], columnspan=data["columnspan"])

    def number_press(self, value):
        print(value)
