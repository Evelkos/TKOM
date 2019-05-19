# bool.py

from .value import Value


class Bool(Value):
    def __init__(self, value, line=None, column=None):
        super().__init__(value, line, column)
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Bool) and self.value == other.value

    def __repr__(self):
        return f"[BOOL: {self.value}]"

    def accept(self, visitor):
        return visitor.visit_bool(self)
