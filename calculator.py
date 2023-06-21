import customtkinter as ctk
from config.settings import *
from widgets import *


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=WINDOW_COLOR)

        self.result = ctk.StringVar(value="0")
        self.equation = ctk.StringVar(value="")

        # window setup
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")

        self.equation_display = equation_widget.EquationWidget(self)
        self.output_display = output_widget.OutputWidget(self)
        self.keypad = keypad_widget.KeypadWidget(self)

        self.equation_display.place(x=0, y=0, relwidth=1, relheight=0.15)
        self.output_display.place(x=0, rely=0.15, relwidth=1, relheight=0.15)
        self.keypad.place(x=0, rely=0.3, relwidth=1, relheight=0.7)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
