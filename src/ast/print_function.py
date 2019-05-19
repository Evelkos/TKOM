#print_function.py

from .node import Node


class PrintFunction(Node):
    def __init__(self, identifier, line=None, column=None):
        super().__init__(line, column)
        self.identifier = identifier
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, PrintFunction) and self.identifier == other.identifier

    def __repr__(self):
        return f"[PRINT: {self.identifier}]"

    def accept(self, visitor):
        return visitor.visit_print_function(self)
