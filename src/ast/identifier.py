# identifier.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "identifier":
    from node import Node
else:
    from .node import Node


class Identifier(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # TODO
    def visit(self):
        return self.name

    def __repr__(self):
        return f"[Identifier: {self.name}]"