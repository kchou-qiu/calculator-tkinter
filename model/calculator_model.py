class CalculatorModel:
    def __init__(self):
        self._index = 0
        self._operands = [0.0, 0.0]
        self._operator = ""
        self._evaluated = False

    @classmethod
    def _remove_decimal_if_whole(cls, number: float) -> float:
        return round(number) if number.is_integer() else number

    def get_equation(self) -> str:
        if self._operands[0] == 0:
            return ""

        equation = f"{CalculatorModel._remove_decimal_if_whole(self._operands[0])}"

        if self._operator:
            equation += f" {self._operator}"

        if self._operands[1] != 0:
            equation += f" {CalculatorModel._remove_decimal_if_whole(self._operands[1])}"

        return equation

    def get_current_number(self) -> float:
        return self._remove_decimal_if_whole(self._operands[self._index])

    def clear(self) -> None:
        self._index = 0
        self._operands[0] = 0.0
        self._operands[1] = 0.0
        self._operator = ""

    def negate(self):
        self._operands[self._index] *= -1

    def percent(self):
        self._operands[self._index] /= 100

    def decimal(self):
        if self._operands[self._index] > 0:
            self._operands[self._index] = (self._operands[self._index] * 10) / 10

    def add_number(self, number: int) -> None:
        self._operands[self._index] = (self._operands[self._index] * 10) + number

    def add_operator(self, operator: str) -> None:
        self._operator = operator
        self._index = (self._index + 1) % len(self._operands)

    def evaluate(self) -> None:
        self._operands[0] = eval(f"{self._operands[0]}{self._operator}{self._operands[1]}")
        self._operands[1] = 0.0
        self._index = 0
        self._operator = ""
        self._evaluated = True
