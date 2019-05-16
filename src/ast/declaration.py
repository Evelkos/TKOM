# declaration.py

from .node import Node

class Declaration(Node):
    def __init__(self, variable_type, identifier, value, line=None, column=None):
        self.line = line
        self.column = column
        self.type = variable_type
        self.identifier = identifier
        self.value = value

    # TODO
    def visit(self):
        return self.elements

    def __repr__(self):
        return f"[Declaration: {self.type}, {self.identifier}, {self.value}]"
