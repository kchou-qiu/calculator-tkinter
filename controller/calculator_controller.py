from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self.model.add_number,
                                   self.model.add_operator,
                                   self.model.clear,
                                   self.model.invert,
                                   self.model.percent,
                                   self.model.evaluate_expression)

    def execute(self):
        self.view.mainloop()
