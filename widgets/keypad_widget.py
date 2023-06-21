import customtkinter as ctk
from config.settings import *


class KeypadWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk) -> None:
        super().__init__(parent)

        # grid layout
        for i in range(KEY_ROWS):
            self.rowconfigure(i, weight=1, uniform="a")

        for j in range(KEY_COLS):
            self.columnconfigure(j, weight=1, uniform="a")

        # buttons
        self.button1 = ctk.CTkButton(self, text="AC")
        self.button2 = ctk.CTkButton(self, text="+/-")
        self.button3 = ctk.CTkButton(self, text="%")
        self.button4 = ctk.CTkButton(self, text="/")

        self.button5 = ctk.CTkButton(self, text="7")
        self.button6 = ctk.CTkButton(self, text="8")
        self.button7 = ctk.CTkButton(self, text="9")
        self.button8 = ctk.CTkButton(self, text="X")

        self.button9 = ctk.CTkButton(self, text="4")
        self.button10 = ctk.CTkButton(self, text="5")
        self.button11 = ctk.CTkButton(self, text="6")
        self.button12 = ctk.CTkButton(self, text="-")

        self.button13 = ctk.CTkButton(self, text="1")
        self.button14 = ctk.CTkButton(self, text="2")
        self.button15 = ctk.CTkButton(self, text="3")
        self.button16 = ctk.CTkButton(self, text="+")

        self.button17 = ctk.CTkButton(self, text="0")
        self.button18 = ctk.CTkButton(self, text=".")
        self.button19 = ctk.CTkButton(self, text="=")

        # button placement
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button2.grid(row=0, column=1, sticky="nsew")
        self.button3.grid(row=0, column=2, sticky="nsew")
        self.button4.grid(row=0, column=3, sticky="nsew")

        self.button5.grid(row=1, column=0, sticky="nsew")
        self.button6.grid(row=1, column=1, sticky="nsew")
        self.button7.grid(row=1, column=2, sticky="nsew")
        self.button8.grid(row=1, column=3, sticky="nsew")

        self.button9.grid(row=2, column=0, sticky="nsew")
        self.button10.grid(row=2, column=1, sticky="nsew")
        self.button11.grid(row=2, column=2, sticky="nsew")
        self.button12.grid(row=2, column=3, sticky="nsew")

        self.button13.grid(row=3, column=0, sticky="nsew")
        self.button14.grid(row=3, column=1, sticky="nsew")
        self.button15.grid(row=3, column=2, sticky="nsew")
        self.button16.grid(row=3, column=3, sticky="nsew")

        self.button17.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.button18.grid(row=4, column=2, sticky="nsew")
        self.button19.grid(row=4, column=3, sticky="nsew")
