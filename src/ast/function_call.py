# function_call.py

from .node import Node


class FunctionCall(Node):
    def __init__(self, function_identifier, arguments, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.identifier = function_identifier
        self.arguments = arguments

    def __eq__(self, other):
        return self.identifier == other.identifier and self.arguments == other.arguments

    def __repr__(self):
        return f"[FunctionCall: {self.identifier}, {self.arguments}]"

    def accept(self, visitor):
        visitor.visit_FunctionCall()
