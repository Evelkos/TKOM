# identifier.py

from .node import Node


class Identifier(Node):
    def __init__(self, name, line=None, column=None):
        super().__init__(line, column)
        self.name = name
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Identifier) and self.name == other.name

    def __repr__(self):
        return f"[Identifier: {self.name}]"

    def accept(self, visitor):
        return visitor.visit_identifier(self)
