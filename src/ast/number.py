# number.py

from .node import Node
from .value import Value

class Number(Value):
    def __init__(self, value, line=None, column=None):
        self.line = line
        self.column = column
        self.value = int(value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"[NUMBER: {self.value}]"

    def accept(self, visitor):
        visitor.visit_Number()
