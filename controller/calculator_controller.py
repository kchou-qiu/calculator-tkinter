from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def execute(self):
        self.view.mainloop()
