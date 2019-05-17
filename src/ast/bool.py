# bool.py

from .node import Node
from .value import Value

class Bool(Value):
    def __init__(self, value, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__(value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"[BOOL: {self.value}]"

    def accept(self, visitor):
        return visitor.visit_Bool(self)
