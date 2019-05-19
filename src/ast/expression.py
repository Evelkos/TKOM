# expression.py

from .node import Node

class Expression(Node):
    def __init__(self, left_operand, operation=None, right_operand=None, line=None, column=None):
        self.line = line
        self.column = column
        self.left_operand = left_operand
        self.operation = operation
        self.right_operand = right_operand

    def __eq__(self, other):
        return isinstance(other, Expression) and self.left_operand == other.left_operand and self.operation == other.operation and self.right_operand == other.right_operand

    def __repr__(self):
        return f"[Expression: {self.left_operand}, {self.operation}, {self.right_operand}]"

    def accept(self, visitor):
        return visitor.visit_Expression(self)
