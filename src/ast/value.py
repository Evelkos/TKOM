# value.py

from .node import Node

class Value(Node):
    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value
        # self.line = line
        # self.column = column

    def __repr__(self):
        return f"[Value: {self.value}]"

    def accept(self, visitor):
        return visitor.visit_value(self)
