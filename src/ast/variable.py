# variable.py

from .node import Node


class Variable(Node):
    def __init__(self, variable_type, variable_identifier, value=None, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.type = variable_type
        self.identifier = variable_identifier
        self.value = value

    def __eq__(self, other):
        return self.type == other.type and self.identifier == other.identifier and self.value == other.value

    def __repr__(self):
        return f"[Variable: {self.type}, {self.identifier}, {self.value}]"

    def accept(self, visitor):
        return visitor.visit_Variable(self)
