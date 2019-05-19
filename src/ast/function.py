# function.py

from .node import Node


class Function(Node):
    def __init__(self, function_identifier, arguments, body, line=None, column=None):
        super().__init__(line, column)
        self.identifier = function_identifier
        self.arguments = arguments
        self.body = body
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return (
                isinstance(other, Function) and
                self.identifier == other.identifier and
                self.arguments == other.arguments and
                self.body == other.body
        )

    def __repr__(self):
        return f"[Function: {self.identifier}, {self.arguments}, {self.body}]"

    def accept(self, visitor):
        return visitor.visit_function(self)
