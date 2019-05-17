# function.py

from .node import Node


class VariableType(Node):
    def __init__(self, type_name, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.type = type_name

    def __repr__(self):
        return f"[Type: {self.type}]"

    def accept(self, visitor):
        return visitor.visit_VariableType(self)
