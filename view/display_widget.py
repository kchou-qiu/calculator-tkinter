import customtkinter as ctk

from assets.styling import DISPLAY_PADDING_MAIN


class DisplayWidget(ctk.CTkFrame):
    """
    A widget containing a single display label.
    """
    def __init__(self, parent: ctk.CTk, anchor: str, font: ctk.CTkFont) -> None:
        super().__init__(parent)
        self._display = ctk.StringVar(self)
        self.label = ctk.CTkLabel(self, textvariable=self._display, font=font, anchor=anchor, padx=DISPLAY_PADDING_MAIN)
        self.label.pack(expand=True, fill="both")

    def update_display(self, text: str) -> None:
        """
        Updates the display.

        Parameters
        ----------
        text: str
            The text to replace original.

        Returns
        -------
        None
        """
        self._display.set(text)
