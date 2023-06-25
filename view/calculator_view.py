from typing import Callable

import customtkinter as ctk

from view.display_widget import EquationDisplayWidget, ResultsDisplayWidget
from view.keypad_widget import KeypadWidget, KeypadButton
from assets.styling import *
from assets.config import *


class CalculatorView(ctk.CTk):
    def __init__(self,
                 on_number: Callable[[str], None],
                 on_operator: Callable[[str], None],
                 on_clear: Callable[[], None],
                 on_invert: Callable[[], None],
                 on_percent: Callable[[], None],
                 on_evaluate: Callable[[], None]):
        super().__init__(fg_color=COLORS["dark-gray"])

        self.result = ctk.StringVar(value="0")
        self.equation = ctk.StringVar(value="")

        # window setup
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")
        self.resizable(False, False)

        self.equation_display = EquationDisplayWidget(self)
        self.results_display = ResultsDisplayWidget(self)
        self.keypad = KeypadWidget(self, KEY_ROWS, KEY_COLS)

        # number buttons
        for number, data in NUMBER_BUTTONS.items():
            KeypadButton(self.keypad,
                         text=number,
                         command=lambda x=number: on_number(x),
                         row=data["row"], column=data["column"],
                         columnspan=data["columnspan"])

        # operator buttons
        for operator, data in OPERATOR_BUTTONS.items():
            KeypadButton(self.keypad,
                         text=operator,
                         command=lambda x=operator: on_operator(x),
                         row=data["row"],
                         column=data["column"],
                         columnspan=data["columnspan"])

        # clear button
        KeypadButton(self.keypad,
                     text="AC",
                     command=on_clear,
                     row=SPECIAL_BUTTONS["clear"]["row"],
                     column=SPECIAL_BUTTONS["clear"]["column"],
                     columnspan=SPECIAL_BUTTONS["clear"]["columnspan"])

        # invert button
        KeypadButton(self.keypad,
                     text="+/-",
                     command=on_invert,
                     row=SPECIAL_BUTTONS["invert"]["row"],
                     column=SPECIAL_BUTTONS["invert"]["column"],
                     columnspan=SPECIAL_BUTTONS["invert"]["columnspan"])

        # percent button
        KeypadButton(self.keypad,
                     text="%",
                     command=on_percent,
                     row=SPECIAL_BUTTONS["percent"]["row"],
                     column=SPECIAL_BUTTONS["percent"]["column"],
                     columnspan=SPECIAL_BUTTONS["percent"]["columnspan"])

        # equal button
        KeypadButton(self.keypad,
                     text="=",
                     command=on_evaluate,
                     row=SPECIAL_BUTTONS["equal"]["row"],
                     column=SPECIAL_BUTTONS["equal"]["column"],
                     columnspan=SPECIAL_BUTTONS["equal"]["columnspan"])

        self.equation_display.place(x=0, y=0, relwidth=1, relheight=0.15)
        self.results_display.place(x=0, rely=0.15, relwidth=1, relheight=0.15)
        self.keypad.place(x=0, rely=0.3, relwidth=1, relheight=0.7)
