# declaration.py

from .node import Node

class Declaration(Node):
    def __init__(self, variable_type, identifier, value, line=None, column=None):
        self.line = line
        self.column = column
        self.type = variable_type
        self.identifier = identifier
        self.value = value

    def __repr__(self):
        return f"[Declaration: {self.type}, {self.identifier}, {self.value}]"

    # TODO
    def accept(self, visitor):
        return visitor.visit_Declaration(self)
