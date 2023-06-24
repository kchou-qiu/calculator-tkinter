import customtkinter as ctk
from view.display_widget import EquationDisplayWidget, ResultsDisplayWidget
from view.keypad_widget import KeypadWidget
from assets.styling import *
from assets.config import *


class CalculatorView(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=COLORS["dark-gray"])

        self.result = ctk.StringVar(value="0")
        self.equation = ctk.StringVar(value="")

        # window setup
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")

        self.equation_display = EquationDisplayWidget(self)
        self.results_display = ResultsDisplayWidget(self)
        self.keypad = KeypadWidget(self)

        self.equation_display.place(x=0, y=0, relwidth=1, relheight=0.15)
        self.results_display.place(x=0, rely=0.15, relwidth=1, relheight=0.15)
        self.keypad.place(x=0, rely=0.3, relwidth=1, relheight=0.7)
