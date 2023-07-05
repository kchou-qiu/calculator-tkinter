from typing import Tuple

from assets.config import MAX_CHARACTER_DISPLAY


class CalculatorModel:
    """
    The model for the calculator.

    Handles all the logic for processing the user's input.
    """
    def __init__(self):
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._clear_next_input = True
        self._was_evaluated = True

        # current, operands, and operator are subject to change and may not reflect original equation
        # store copy of original operands and operator, so equation can be reassembled in the future
        self._equation_left = ""
        self._equation_right = ""
        self._equation_operator = ""

    @staticmethod
    def evaluate(left: str, right: str, operator: str) -> str:
        """
        Evaluates the given expression.

        Parameters
        ----------
        left: str
            The left operand.
        right: str
            The right operand.
        operator: str
            The operator.

        Returns
        -------
        str
            The results of the calculation.
        """
        return str(eval(f"{left}{operator}{right}"))

    def get_equation(self) -> Tuple[str, str, str]:
        """
        Gets the components of the equation.

        Returns
        -------
        Tuple[str, str, str]
            A tuple containing, in order, the left operand, right operand, and operator.
        """
        return self._equation_left, self._equation_right, self._equation_operator

    def _set_equation(self, left: str = "", right: str = "", operator: str = "") -> None:
        """
        Sets the components of the equations.

        Parameters
        ----------
        left: str
            The left operand.
        right: str
            The right operand.
        operator: str
            The operator.

        Returns
        -------
        None
        """
        self._equation_left = left
        self._equation_right = right
        self._equation_operator = operator

    def get_result(self) -> str:
        """
        Gets the current results.

        Returns
        -------
        str
            The current results.
        """
        return self._current

    def clear(self) -> None:
        """
        Resets all data and logic.

        Returns
        -------
        None
        """
        self._index = 0
        self._operands = ["0", ""]
        self._operator = ""
        self._current = self._operands[self._index]
        self._set_equation()
        self._clear_next_input = True
        self._was_evaluated = True

    def negate(self) -> None:
        """
        Applies negation to the current number. If the number is positive, it becomes negative. If the number is
        negative, it becomes positive.

        Returns
        -------
        None
        """
        if self._current and self._current != "0":
            if self._current[0] != "-":
                self._current = "-" + self._current[:]
            else:
                self._current = self._current[1:]

            self._operands[self._index] = self._current

    def percent(self) -> None:
        """
        Divides the current number by 100.

        Returns
        -------
        None
        """
        if self._current and self._current != "0":
            # adjusting for when user's enter any "x." type inputs
            if self._current.endswith("."):
                self._current += "0"

            self._operands[self._index] = str(float(self._current) / 100)
            self._current = self._operands[self._index]

    def decimal(self) -> None:
        """
        Appends a decimal to the current number if it doesn't already have one.

        Returns
        -------
        None
        """
        if self._clear_next_input:
            self._operands[self._index] = "0"
            self._current = "0."
            self._clear_next_input = False
        elif float(self._current).is_integer() and not self._current == "0.":
            # check to ensure decimal can only be added once
            self._operands[self._index] += "."
            self._current = self._operands[self._index]

    def add_number(self, number: str) -> None:
        """
        Appends a number to the current number.

        Parameters
        ----------
        number: str
            The number to be appended.

        Returns
        -------
        None
        """
        if self._clear_next_input:
            self._clear_next_input = False
            self._current = number
        elif len(self._current) < MAX_CHARACTER_DISPLAY:
            self._current += number

        # keep the current number and the corresponding operand aligned
        self._operands[self._index] = self._current

    def add_operator(self, operator: str) -> None:
        """
        Sets the current operator, replacing the previous one if the full expression has not been set.

        If the expression has already been completed, automatically evaluates the expression then uses the result
        as the new left operand before setting the new operator.

        Parameters
        ----------
        operator:
            The operator to set.

        Returns
        -------
        None
        """
        if self._clear_next_input or self._was_evaluated:
            self._operands[1] = ""
            self._was_evaluated = False
        elif self._operator and self._operands[1]:
            # make space for new operator by evaluating previous expression
            self._operands[0] = self.evaluate(self._operands[0], self._operands[1], self._operator)
            self._operands[1] = ""
            self._current = self._operands[0]
            # important to reset index to 0 otherwise index will become unaligned
            self._index = 0

        self._clear_next_input = True
        self._set_equation(self._operands[0], operator=operator)
        self._operator = operator

        # moves operand pointer to next operand or loop back to first
        self._index = (self._index + 1) % len(self._operands)

    def equal(self) -> None:
        """
        Evaluates the current expression. Immediate sequential evaluations without new number or operator inputs
        replaces the original left operand with the result.

        If only the left operand and operator has been set, the expression is treated as if the first operand
        was entered twice. For example, "5 + " is evaluated as "5 + 5" = 10.

        If only the left operand is set, the result is the left operand.

        Returns
        -------
        None
        """
        # if second operand not given, treat it as shortcut to duplicate first operand
        if self._operator and not self._operands[1]:
            self._operands[1] = self._operands[0]

        self._set_equation(self._operands[0], self._operands[1], self._operator)

        try:
            self._operands[0] = self.evaluate(self._operands[0], self._operands[1], self._operator)
        except ZeroDivisionError:
            self.clear()
            raise ZeroDivisionError
        else:
            # keep previous operator and second operand to allow user to press "=" consecutively
            self._index = 0
            self._current = self._operands[0]
            self._clear_next_input = True
            self._was_evaluated = True
