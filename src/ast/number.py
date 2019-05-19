# number.py

from .value import Value


class Number(Value):
    def __init__(self, value, line=None, column=None):
        super().__init__(value, line, column)
        self.value = int(value)
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Number) and self.value == other.value

    def __repr__(self):
        return f"[NUMBER: {self.value}]"

    def accept(self, visitor):
        return visitor.visit_number(self)
