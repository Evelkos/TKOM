# function.py

from .node import Node


class Function(Node):
    def __init__(self, function_identifier, arguments, body, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.identifier = function_identifier
        self.arguments = arguments
        self.body = body

    def __eq__(self, other):
        return self.identifier == other.identifier and self.arguments == other.arguments and self.body == other.body

    def __repr__(self):
        return f"[Function: {self.identifier}, {self.arguments}, {self.body}]"

    def accept(self, visitor):
        visitor.visit_Function()
