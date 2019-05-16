# value.py

from .node import Node

class Value(Node):
    def __init__(self, value, line=None, column=None):
        self.line = line
        self.column = column
        self.value = value

    # TODO
    def visit(self):
        return self.value

    def __repr__(self):
        return f"[Value: {self.value}]"