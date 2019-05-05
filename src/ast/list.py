# list.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "list":
    from node import Node
else:
    from .node import Node

class List(Node):
    def __init__(self, elements):
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
    # TODO
    
    def visit(self):
        return self.elements

    def length(self):
        return len(self.elements)

    def get(self, idx):
        if idx < len(self.elements):
            return elements[idx]
        return None