from controller.calculator_controller import CalculatorController
from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView

if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    app = CalculatorController(model, view)
    app.run()
