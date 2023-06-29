from typing import Tuple

from assets.config import DEFAULT_RESULTS


class CalculatorModel:
    def __init__(self):
        self._index = 0
        self._operands = [DEFAULT_RESULTS, ""]
        self._operator = ""
        self._current_number = DEFAULT_RESULTS
        self._evaluated = False

    def get_equation(self):
        return f"{self._operands[0]} {self._operator} {self._operands[1]}"

    def get_current_number(self):
        return self._current_number

    def clear(self) -> None:
        self._index = 0
        self._operands[0] = DEFAULT_RESULTS
        self._operands[1] = ""
        self._operator = ""
        self._current_number = DEFAULT_RESULTS

    def invert(self):
        print("invert")

    def percent(self):
        print("percent")

    def decimal(self):
        print("decimal")

    def add_number(self, number: str) -> None:
        if self._evaluated:
            self._evaluated = False
            self.clear()

        if self._operands[self._index] == DEFAULT_RESULTS:
            self._operands[self._index] = ""

        self._operands[self._index] += number
        self._current_number = self._operands[self._index]

    def add_operator(self, operator: str) -> None:
        if self._evaluated:
            self._evaluated = False

        self._operator = operator
        self._index = (self._index + 1) % len(self._operands)

    def evaluate(self) -> None:
        self._operands[0] = str(eval(f"{self._operands[0]}{self._operator}{self._operands[1]}"))
        self._operands[1] = ""
        self._index = 0
        self._operator = ""
        self._current_number = self._operands[0]
        self._evaluated = True
