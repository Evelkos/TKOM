# expression.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "expression":
    from node import Node
else:
    from .node import Node

class Expression(Node):
    def __init__(self, left_operand, operation=None, right_operand=None):
        self.left_operand = left_operand
        self.operation = operation
        self.right_operand = right_operand

    # TODO
    def visit(self):
        return self.elements

    def __repr__(self):
        return f"[Expression: {self.left_operand}, {self.operation}, {self.right_operand}]"
