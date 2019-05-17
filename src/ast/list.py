# list.py

from .node import Node

class List(Node):
    def __init__(self, elements, line=None, column=None):
        self.line = line
        self.column = column
        self.elements = elements

    def __eq__(self, other):
        if self.length() == other.length():
            for idx in range(0, len(self.elements) - 1):
                if self.elements[idx] != other.elements[idx]:
                    return False
            return True
        return False

    def __repr__(self):
        buff = f"[LIST:"
        for element in self.elements:
            buff += f" {element}"
        buff += "]"
        return buff

    def accept(self, visitor):
        visitor.visit_List()

    def get(self, idx):
        if idx < len(self.elements):
            return elements[idx]
        return None

    def length(self):
        return len(self.elements)
