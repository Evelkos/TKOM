# bool.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "list":
    from node import Node
else:
    from .node import Node

class List(Node):
    def __init__(self, elements):
        self.elements = elements

    # TODO
    def visit(self):
        return self.elements

    def __repr__(self):
        buff = f"[LIST:"
        for element in self.elements:
            buff += f" {element}"
        buff += "]"
        return buff