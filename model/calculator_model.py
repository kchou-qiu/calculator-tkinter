class CalculatorModel:
    def __init__(self):
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._equation = ""
        self._clear_next_input = True

    @staticmethod
    def evaluate(left: str, right: str, operator: str) -> str:
        return str(eval(f"{left}{operator}{right}"))

    @staticmethod
    def clean_decimal(number: str) -> str:
        if number.endswith("."):
            number += "0"
        converted = float(number)
        return str(int(converted)) if converted.is_integer() else number

    def get_equation(self) -> str:
        return self._equation

    def _set_equation(self, left: str = "", right: str = "", operator: str = "", is_evaluated: bool = False):
        self._equation = ""

        if left:
            self._equation += f"{self.clean_decimal(left)}"

        if operator:
            self._equation += f" {operator}"

        if right:
            self._equation += f" {self.clean_decimal(right)}"

        if is_evaluated:
            self._equation += " ="

    def get_result(self) -> str:
        return self._current

    def clear(self) -> None:
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._set_equation()
        self._clear_next_input = True

    def negate(self):
        if self._current and self._current != "0":
            if self._current[0] != "-":
                self._current = "-" + self._current[:]
            else:
                self._current = self._current[1:]

            self._operands[self._index] = self._current

    def percent(self):
        if self._current and self._current != "0":
            if self._current.endswith("."):
                self._current += "0"

            self._operands[self._index] = str(float(self._current) / 100)
            self._current = self.clean_decimal(self._operands[self._index])

    def decimal(self):
        if self._clear_next_input:
            self._clear_next_input = False
            self._operands[0] = "0"
            self._current = "0."
        elif float(self._current).is_integer() and not self._current == "0.":
            self._operands[self._index] += "."
            self._current = self._operands[self._index]

    def add_number(self, number: str) -> None:
        if self._clear_next_input:
            self._current = number
            self._clear_next_input = False
        else:
            self._current += number

        self._operands[self._index] = self._current

    def add_operator(self, operator: str) -> None:
        if self._clear_next_input:
            self._operands[1] = ""
        elif self._operator and self._operands[1]:
            # make space for new expression by first evaluating previous expression
            self._operands[0] = self.evaluate(self._operands[0], self._operands[1], operator)
            self._operands[1] = ""

        self._operator = operator
        self._index = (self._index + 1) % len(self._operands)
        self._set_equation(self._operands[0], operator=operator)
        self._clear_next_input = True

    def equal(self) -> None:
        # if second operand not given, treat it as shortcut to duplicate first operand
        if self._operator and not self._operands[1]:
            self._operands[1] = self._operands[0]

        self._set_equation(self._operands[0], self._operands[1], self._operator, True)
        self._operands[0] = self.evaluate(self._operands[0], self._operands[1], self._operator)
        self._current = self.clean_decimal(self._operands[0])
        self._index = 0
        self._clear_next_input = True
