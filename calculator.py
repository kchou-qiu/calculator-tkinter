import customtkinter as ctk
from config.settings import *
from widgets import *


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=WINDOW_COLOR)

        # window setup
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")
        self.resizable(False, False)

        # layout
        for i in range(GRID_ROWS):
            self.rowconfigure(i, weight=1)

        for j in range(GRID_COLS):
            self.columnconfigure(j, weight=1)

        # widgets
        self.equation_display = equation_widget.EquationWidget(self)
        self.results_display = output_widget.OutputWidget(self)
        self.keypad = keypad_widget.KeypadWidget(self)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
