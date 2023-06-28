from assets.config import NumberButtons, SpecialButtons, OperatorButtons, DEFAULT_RESULTS, DEFAULT_EQUATION
from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView) -> None:
        self.model = model
        self.view = view
        self._bind_buttons()

        self.view.update_ui(DEFAULT_RESULTS, DEFAULT_EQUATION)

    def _bind_buttons(self):
        for number in NumberButtons:
            self.view.bind_number_operator_button(number, self.add_number)

        for operator in OperatorButtons:
            self.view.bind_number_operator_button(operator, self.add_operator)

        self.view.bind_special_button(SpecialButtons.CLEAR, self.clear)
        self.view.bind_special_button(SpecialButtons.INVERT, self.invert)
        self.view.bind_special_button(SpecialButtons.PERCENT, self.percent)
        self.view.bind_special_button(SpecialButtons.DECIMAL, self.decimal)
        self.view.bind_special_button(SpecialButtons.EQUAL, self.evaluate)

    def clear(self):
        self.model.clear()

    def invert(self):
        self.model.invert()

    def percent(self):
        self.model.percent()

    def decimal(self):
        self.model.decimal()

    def add_number(self, number: str) -> None:
        self.model.add_number(number)

    def add_operator(self, operator: str) -> None:
        self.model.add_operator(operator)

    def evaluate(self) -> None:
        self.model.evaluate()

    def run(self):
        self.view.mainloop()
