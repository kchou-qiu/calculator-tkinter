from typing import Callable

import customtkinter as ctk

from view.display_widget import DisplayWidget
from view.keypad_widget import KeypadWidget, KeypadButton
from assets.styling import *
from assets.config import *


class CalculatorView(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=COLOR_FOREGROUND)
        self._buttons = {}

        # display widgets
        self._equation_widget = DisplayWidget(self, "se", ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE_DISPLAY_EQUATION))
        self._results_widget = DisplayWidget(self, "e", ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE_DISPLAY_RESULTS))
        self._keypad_widget = KeypadWidget(self, KEY_ROWS, KEY_COLS)

        # UI
        self._create_ui()
        self._create_buttons(self._keypad_widget)

    def _create_ui(self) -> None:
        # window setup
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")
        self.resizable(False, False)

        # master ui layout
        self._equation_widget.place(**EQUATION_LAYOUT)
        self._results_widget.place(**RESULTS_LAYOUT)
        self._keypad_widget.place(**KEYPAD_LAYOUT)

    def _create_buttons(self, parent: ctk.CTkFrame) -> None:
        font_main = ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE_BUTTONS_1)
        font_secondary = ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE_BUTTONS_2)
        font_tertiary = ctk.CTkFont(family=FONT_FAMILY, size=FONT_SIZE_BUTTONS_3)

        self._buttons.update({
            name: KeypadButton(parent,
                               COLOR_BUTTON_NUMBERS,
                               data["text"],
                               data["value"],
                               data["row"],
                               data["column"],
                               data["columnspan"],
                               font_main)
            for name, data in NUMBER_BUTTONS.items()
        })

        self._buttons.update({
            name: KeypadButton(parent,
                               COLOR_BUTTON_OPERATOR,
                               data["text"],
                               data["value"],
                               data["row"],
                               data["column"],
                               data["columnspan"],
                               font_main)
            for name, data in OPERATOR_BUTTONS.items()
        })

        self._buttons.update({
            name: KeypadButton(parent,
                               COLOR_BUTTON_SPECIAL,
                               data["text"],
                               data["value"],
                               data["row"],
                               data["column"],
                               data["columnspan"],
                               font_main)
            for name, data in SPECIAL_BUTTONS.items()
        })

        self._buttons[SpecialButtons.DECIMAL].configure(fg_color=COLOR_BUTTON_NUMBERS)
        self._buttons[SpecialButtons.EQUAL].configure(fg_color=COLOR_BUTTON_EXTRA)
        self._buttons[OperatorButtons.DIVISION].configure(font=font_secondary)
        self._buttons[OperatorButtons.SUBTRACTION].configure(font=font_tertiary)

    def bind_number_operator_button(self, name: Enum, callback: Callable[[str], None]) -> None:
        if name not in self._buttons:
            raise KeyError(f"{name} button does not exist.")

        button = self._buttons[name]
        button.configure(command=lambda value=button.value:  callback(value))

    def bind_special_button(self, name: Enum, callback: Callable[[], None]) -> None:
        if name not in self._buttons:
            raise KeyError(f"{name} button does not exist.")

        button = self._buttons[name]
        button.configure(command=callback)

    def update_ui(self, results: str, expression: str) -> None:
        self._results_widget.update_display(results)
        self._equation_widget.update_display(expression)
