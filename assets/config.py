from enum import Enum


class NumberButtons(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class OperatorButtons(Enum):
    DIVISION = 0
    MULTIPLICATION = 1
    SUBTRACTION = 2
    ADDITION = 3


class SpecialButtons(Enum):
    CLEAR = 0
    INVERT = 1
    PERCENT = 2
    DECIMAL = 3
    EQUAL = 4


# window
APP_TITLE = "Calculator"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
WINDOW_COLOR = ""

# grid layout for keypad
KEY_ROWS = 5
KEY_COLS = 4

DEFAULT_RESULTS = "0"
DEFAULT_EQUATION = ""

# button data and layout
NUMBER_BUTTONS = {
    NumberButtons.SEVEN: {"row": 1, "column": 0, "columnspan": 1, "text": "7", "value": "7"},
    NumberButtons.EIGHT: {"row": 1, "column": 1, "columnspan": 1, "text": "8", "value": "8"},
    NumberButtons.NINE: {"row": 1, "column": 2, "columnspan": 1, "text": "9", "value": "9"},
    NumberButtons.FOUR: {"row": 2, "column": 0, "columnspan": 1, "text": "4", "value": "4"},
    NumberButtons.FIVE: {"row": 2, "column": 1, "columnspan": 1, "text": "5", "value": "5"},
    NumberButtons.SIX: {"row": 2, "column": 2, "columnspan": 1, "text": "6", "value": "6"},
    NumberButtons.ONE: {"row": 3, "column": 0, "columnspan": 1, "text": "1", "value": "1"},
    NumberButtons.TWO: {"row": 3, "column": 1, "columnspan": 1, "text": "2", "value": "2"},
    NumberButtons.THREE: {"row": 3, "column": 2, "columnspan": 1, "text": "3", "value": "3"},
    NumberButtons.ZERO: {"row": 4, "column": 0, "columnspan": 2, "text": "0", "value": "0"},
}

OPERATOR_BUTTONS = {
    OperatorButtons.DIVISION: {"row": 0, "column": 3, "columnspan": 1, "text": "\u00f7", "value": "/"},
    OperatorButtons.MULTIPLICATION: {"row": 1, "column": 3, "columnspan": 1, "text": "x", "value": "*"},
    OperatorButtons.SUBTRACTION: {"row": 2, "column": 3, "columnspan": 1, "text": "-", "value": "-"},
    OperatorButtons.ADDITION: {"row": 3, "column": 3, "columnspan": 1, "text": "+", "value": "+"},
}

SPECIAL_BUTTONS = {
    SpecialButtons.CLEAR: {"row": 0, "column": 0, "columnspan": 1, "text": "AC", "value": "Clear"},
    SpecialButtons.INVERT: {"row": 0, "column": 1, "columnspan": 1, "text": "\u00b1", "value": "Invert"},
    SpecialButtons.PERCENT: {"row": 0, "column": 2, "columnspan": 1, "text": "%", "value": "Percentage"},
    SpecialButtons.EQUAL: {"row": 4, "column": 3, "columnspan": 1, "text": "=", "value": "Evaluate"},
    SpecialButtons.DECIMAL: {"row": 4, "column": 2, "columnspan": 1, "text": ".", "value": "Decimal"}
}
