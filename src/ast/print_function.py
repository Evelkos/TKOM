#print_function.py

from .node import Node

class PrintFunction(Node):
    def __init__(self, identifier, line=None, column=None):
        self.line = line
        self.column = column
        self.identifier = identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __repr__(self):
        return f"[PRINT: {self.identifier}]"

    def accept(self, visitor):
        return visitor.visit_PrintFunction(self)
