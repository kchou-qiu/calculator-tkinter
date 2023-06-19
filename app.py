import customtkinter as ctk
import darkdetect
from Config.config import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window setup
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
                      f"+{(self.winfo_screenwidth() - WINDOW_WIDTH) // 2}"
                      f"+{(self.winfo_screenheight() - WINDOW_HEIGHT) // 2}")
        self.resizable(False, False)


if __name__ == "__main__":
    print(darkdetect.isDark())
    app = App()
    app.mainloop()
