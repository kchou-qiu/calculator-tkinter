class CalculatorModel:
    def __init__(self):
        self._left_side = ""
        self._operator = ""
        self._right_side = ""

    def clear(self):
        print("clear")

    def invert(self):
        print("invert")

    def percent(self):
        print("percent")

    def decimal(self):
        print("decimal")

    def add_number(self, number: str) -> None:
        print(number)

    def add_operator(self, operator: str) -> None:
        print(operator)

    def evaluate(self) -> None:
        print("evalulate!")
