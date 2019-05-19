# list.py

from .node import Node


class List(Node):
    def __init__(self, elements, line=None, column=None):
        super().__init__(line, column)
        self.elements = elements
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        if isinstance(other, List) and self.length() == other.length():
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
        return visitor.visit_list(self)

    def get(self, idx):
        if idx < len(self.elements):
            return self.elements[idx]
        return None

    def length(self):
        return len(self.elements)
