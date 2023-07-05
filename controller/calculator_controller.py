from assets.config import NumberButtons, SpecialButtons, OperatorButtons, ZERO_DIVISION, MAX_CHARACTER_DISPLAY, PRECISION
from model.calculator_model import CalculatorModel
from view.calculator_view import CalculatorView


class CalculatorController:
    """The controller component of the calculator.

    Intermediary that connects the user interface to the logic. Accepts user key input from GUI then sends it to
    the model for processing. Once processed, the controller formats the results then sends over to the view to be
    displayed.
    """
    def __init__(self, model: CalculatorModel, view: CalculatorView) -> None:
        self.model = model
        self.view = view
        self._bind_buttons()
        self.clear()

    @staticmethod
    def format_number(number: str) -> str:
        """
        Formats the given number string to within the calculator's display. Automatically converts very large
        or very small numbers to exponential notation.

        Parameters
        ----------
        number: str
            The number string to be formatted.

        Returns
        -------
        str
            The formatted number string.
        """
        if not number:
            return number

        # must change "x." -> "x.0" before it can be converted to a number
        if number.endswith("."):
            number += "0"

        return f"{float(number):{MAX_CHARACTER_DISPLAY}.{PRECISION}g}".lstrip(" ")

    def _bind_buttons(self) -> None:
        """
        Assigns callback functions to the GUI's buttons.

        Returns
        -------
        None
        """
        for number in NumberButtons:
            self.view.bind_number_operator_button(number, self.add_number)

        for operator in OperatorButtons:
            self.view.bind_number_operator_button(operator, self.add_operator)

        self.view.bind_special_button(SpecialButtons.CLEAR, self.clear)
        self.view.bind_special_button(SpecialButtons.NEGATE, self.negate)
        self.view.bind_special_button(SpecialButtons.PERCENT, self.percent)
        self.view.bind_special_button(SpecialButtons.DECIMAL, self.decimal)
        self.view.bind_special_button(SpecialButtons.EQUAL, self.evaluate)

    def clear(self) -> None:
        """
        Callback function for clear button.

        Resets the model and view.

        Returns
        -------
        None
        """
        self.model.clear()
        self._update_ui(False, False)

    def negate(self) -> None:
        """
        Callback function for negate button.

        Applies negation on the number currently displayed.

        Returns
        -------
        None
        """
        self.model.negate()
        self._update_ui(False) if self.model.get_result().endswith(".") else self._update_ui()

    def percent(self):
        """
        Callback function for percent button.

        Divides currently displayed number by 100 and updates the display.

        Returns
        -------
        None
        """
        self.model.percent()
        self._update_ui()

    def decimal(self) -> None:
        """
        Callback function for decimal button.

        Appends a decimal to the currently displayed number and updates the display

        Returns
        -------
        None
        """
        self.model.decimal()
        self._update_ui(False)

    def add_number(self, number: str) -> None:
        """
        Callback function for number buttons.

        Appends a number the currently displayed number and updates the display.

        Parameters
        ----------
        number: str
            The number to append.

        Returns
        -------
        None
        """
        self.model.add_number(number)
        self._update_ui(False)

    def add_operator(self, operator: str) -> None:
        """
        Callback function for operator buttons.

        Sets the operator to be used for evaluation and updates the display with the partial expression.

        Parameters
        ----------
        operator: str
            The operator to be evaluated in the expression.

        Returns
        -------
        None
        """
        self.model.add_operator(operator)
        self._update_ui()

    def evaluate(self) -> None:
        """
        Callback function for the equal button.

        Calculates the current expression. Updates the display using the results and equation that was evaluated.

        Returns
        -------
        None
        """
        try:
            self.model.equal()
        except ZeroDivisionError:
            self.view.update_ui(ZERO_DIVISION, "")
        else:
            self._update_ui(include_equal=True)

    def _update_ui(self, format_result: bool = True, format_equation: bool = True, include_equal: bool = False) -> None:
        """
        Updates the calculator's displays.

        Parameters
        ----------
        format_result: bool
            Toggle for whether to format the result. By default, set to True.
        format_equation: bool
            Toggle for whether to format the numbers in the equation. By default, set to True.
        include_equal: bool
            Toggle for whether to include an equal sign ("=") at the end of the equation. By default, set to False.

        Returns
        -------
        None
        """
        result = self.model.get_result()
        left, right, operator = self.model.get_equation()

        if format_result:
            result = self.format_number(result)

        if format_equation:
            left = self.format_number(left)
            right = self.format_number(right)

        self.view.update_ui(result, f"{left} {operator} {right} =" if include_equal else f"{left} {operator} {right}")

    def run(self) -> None:
        """
        Starts the calculator app.

        Returns
        -------
        None
        """
        self.view.mainloop()
