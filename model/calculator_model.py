from typing import Tuple

from assets.config import MAX_CHARACTER_DISPLAY


class CalculatorModel:
    def __init__(self):
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._clear_next_input = True
        self._was_evaluated = True

        # current, operands, and operator are subject to change and may not reflect original equation
        # store copy of original operands and operator, so equation can be reassembled in the future
        self._equation_left = ""
        self._equation_right = ""
        self._equation_operator = ""

    @staticmethod
    def evaluate(left: str, right: str, operator: str) -> str:
        return str(eval(f"{left}{operator}{right}"))

    def get_equation(self) -> Tuple[str, str, str]:
        return self._equation_left, self._equation_right, self._equation_operator

    def _set_equation(self, left: str = "", right: str = "", operator: str = ""):
        self._equation_left = left
        self._equation_right = right
        self._equation_operator = operator

    def get_result(self) -> str:
        return self._current

    def clear(self) -> None:
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._set_equation()
        self._clear_next_input = True
        self._was_evaluated = True

    def negate(self):
        if self._current and self._current != "0":
            if self._current[0] != "-":
                self._current = "-" + self._current[:]
            else:
                self._current = self._current[1:]

            self._operands[self._index] = self._current

    def percent(self):
        if self._current and self._current != "0":
            # adjusting for when user's enter any "x." type inputs
            if self._current.endswith("."):
                self._current += "0"

            self._operands[self._index] = str(float(self._current) / 100)
            self._current = self._operands[self._index]

    def decimal(self):
        if self._clear_next_input:
            self._operands[self._index] = "0"
            self._current = "0."
            self._clear_next_input = False
        elif float(self._current).is_integer() and not self._current == "0.":
            # check to ensure decimal can only be added once
            self._operands[self._index] += "."
            self._current = self._operands[self._index]

    def add_number(self, number: str) -> None:
        if self._clear_next_input:
            self._clear_next_input = False
            self._current = number
        elif len(self._current) < MAX_CHARACTER_DISPLAY:
            self._current += number

        self._operands[self._index] = self._current

    def add_operator(self, operator: str) -> None:
        if self._clear_next_input or self._was_evaluated:
            self._operands[1] = ""
            self._was_evaluated = False
        elif self._operator and self._operands[1]:
            # make space for new operator by evaluating previous expression
            self._operands[0] = self.evaluate(self._operands[0], self._operands[1], self._operator)
            self._operands[1] = ""
            self._current = self._operands[0]
            # important to reset index to 0 otherwise index will become unaligned
            self._index = 0

        self._clear_next_input = True
        self._set_equation(self._operands[0], operator=operator)
        self._operator = operator

        # moves operand pointer to next operand or loop back to first
        self._index = (self._index + 1) % len(self._operands)

    def equal(self) -> None:
        # if second operand not given, treat it as shortcut to duplicate first operand
        if self._operator and not self._operands[1]:
            self._operands[1] = self._operands[0]

        self._set_equation(self._operands[0], self._operands[1], self._operator)

        try:
            self._operands[0] = self.evaluate(self._operands[0], self._operands[1], self._operator)
        except ZeroDivisionError:
            self.clear()
            raise ZeroDivisionError
        else:
            # keep previous operator and second operand to allow user to press "=" consecutively
            self._index = 0
            self._current = self._operands[0]
            self._clear_next_input = True
            self._was_evaluated = True
