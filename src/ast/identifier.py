# identifier.py

from .node import Node


class Identifier(Node):
    def __init__(self, name, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"[Identifier: {self.name}]"

    def accept(self, visitor):
        visitor.visit_Identifier()
