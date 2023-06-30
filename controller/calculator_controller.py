from assets.config import NumberButtons, SpecialButtons, OperatorButtons
from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView) -> None:
        self.model = model
        self.view = view
        self._bind_buttons()
        self.clear()

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
        self.update_ui()

    def negate(self):
        self.model.negate()
        self.update_ui()

    def percent(self):
        self.model.percent()
        self.update_ui()

    def decimal(self):
        self.model.decimal()
        self.update_ui()

    def add_number(self, number: int) -> None:
        self.model.add_number(number)
        self.update_ui()

    def add_operator(self, operator: str) -> None:
        self.model.add_operator(operator)
        self.update_ui()

    def evaluate(self) -> None:
        self.model.evaluate()
        self.update_ui()

    def update_ui(self):
        self.view.update_ui(self.model.get_current_number(), self.model.get_equation())

    def run(self):
        self.view.mainloop()
