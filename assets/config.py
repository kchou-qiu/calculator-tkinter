# window
APP_TITLE = "Calculator"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
WINDOW_COLOR = ""

# grid layout for keypad
KEY_ROWS = 5
KEY_COLS = 4

DEFAULT_VALUE = 0
OPERATOR_SYMBOLS = ["+", "-", "/", "*"]

NUMBER_BUTTONS = {
    "7": {"row": 1, "column": 0, "columnspan": 1},
    "8": {"row": 1, "column": 1, "columnspan": 1},
    "9": {"row": 1, "column": 2, "columnspan": 1},
    "4": {"row": 2, "column": 0, "columnspan": 1},
    "5": {"row": 2, "column": 1, "columnspan": 1},
    "6": {"row": 2, "column": 2, "columnspan": 1},
    "1": {"row": 3, "column": 0, "columnspan": 1},
    "2": {"row": 3, "column": 1, "columnspan": 1},
    "3": {"row": 3, "column": 2, "columnspan": 1},
    "0": {"row": 4, "column": 0, "columnspan": 2},
    ".": {"row": 4, "column": 2, "columnspan": 1, "image": None}
}

OPERATOR_BUTTONS = {
    "/": {"row": 0, "column": 3, "columnspan": 1, "image": None},
    "*": {"row": 1, "column": 3, "columnspan": 1, "image": None},
    "-": {"row": 2, "column": 3, "columnspan": 1, "image": None},
    "+": {"row": 3, "column": 3, "columnspan": 1, "image": None},
}

SPECIAL_BUTTONS = {
    "clear": {"row": 0, "column": 0, "columnspan": 1, "image": None},
    "invert": {"row": 0, "column": 1, "columnspan": 1, "image": None},
    "percent": {"row": 0, "column": 2, "columnspan": 1, "image": None},
    "equal": {"row": 4, "column": 3, "columnspan": 1, "image": None}
}