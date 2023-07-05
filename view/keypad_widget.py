import customtkinter as ctk

from assets.styling import COLOR_FOREGROUND, BUTTON_CORNER_RADIUS, BUTTON_PAD_X, BUTTON_PAD_Y


class KeypadButton(ctk.CTkButton):
    """
    A button of the keypad.
    """
    def __init__(self,
                 parent: ctk.CTkFrame,
                 fg_color,
                 text: str = "",
                 value: str = "",
                 row: int = 0,
                 column: int = 0,
                 columnspan: int = 0,
                 font: ctk.CTkFont = None) -> None:
        super().__init__(parent, text=text,
                         fg_color=fg_color,
                         corner_radius=BUTTON_CORNER_RADIUS,
                         border_color=COLOR_FOREGROUND)
        self._value = value
        self.grid(row=row,
                  column=column,
                  columnspan=columnspan,
                  sticky="NSEW",
                  padx=BUTTON_PAD_X,
                  pady=BUTTON_PAD_Y)

        if font:
            self.configure(font=font)

    @property
    def value(self) -> str:
        """
        Gets the value of the button.

        Returns
        -------
        str
            The value of the button.
        """
        return self._value


class KeypadWidget(ctk.CTkFrame):
    """
    An empty keypad widget with a set grid layout.
    """
    def __init__(self, parent: ctk.CTk, max_rows: int, max_columns: int) -> None:
        super().__init__(parent)

        # grid layout
        for i in range(max_rows):
            self.rowconfigure(i, weight=1, uniform="a")

        for j in range(max_columns):
            self.columnconfigure(j, weight=1, uniform="a")
