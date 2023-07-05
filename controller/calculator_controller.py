from assets.config import NumberButtons, SpecialButtons, OperatorButtons, ZERO_DIVISION, MAX_CHARACTER_DISPLAY, PRECISION
from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView) -> None:
        self.model = model
        self.view = view
        self._bind_buttons()
        self.clear()

    @staticmethod
    def format_number(number: str) -> str:
        if not number:
            return number

        # must change "x." -> "x.0" before it can be converted to a number
        if number.endswith("."):
            number += "0"

        return f"{float(number):{MAX_CHARACTER_DISPLAY}.{PRECISION}g}".lstrip(" ")

    def _bind_buttons(self):
        for number in NumberButtons:
            self.view.bind_number_operator_button(number, self.add_number)

        for operator in OperatorButtons:
            self.view.bind_number_operator_button(operator, self.add_operator)

        self.view.bind_special_button(SpecialButtons.CLEAR, self.clear)
        self.view.bind_special_button(SpecialButtons.NEGATE, self.negate)
        self.view.bind_special_button(SpecialButtons.PERCENT, self.percent)
        self.view.bind_special_button(SpecialButtons.DECIMAL, self.decimal)
        self.view.bind_special_button(SpecialButtons.EQUAL, self.evaluate)

    def clear(self):
        self.model.clear()
        self._update_ui(False, False)

    def negate(self):
        self.model.negate()
        self._update_ui(False)

    def percent(self):
        self.model.percent()
        self._update_ui()

    def decimal(self):
        self.model.decimal()
        self._update_ui(False)

    def add_number(self, number: str) -> None:
        self.model.add_number(number)
        self._update_ui(False)

    def add_operator(self, operator: str) -> None:
        self.model.add_operator(operator)
        self._update_ui()

    def evaluate(self) -> None:
        try:
            self.model.equal()
        except ZeroDivisionError:
            self.view.update_ui(ZERO_DIVISION, "")
        else:
            self._update_ui()

    def _update_ui(self, format_result: bool = True, format_equation: bool = True) -> None:
        result = self.model.get_result()
        left, right, operator = self.model.get_equation()

        if format_result:
            result = self.format_number(result)

        if format_equation:
            left = self.format_number(left)
            right = self.format_number(right)

        self.view.update_ui(result, f"{left} {operator} {right}")

    def run(self):
        self.view.mainloop()
