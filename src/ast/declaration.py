# declaration.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "declaration":
    from node import Node
else:
    from .node import Node

class Declaration(Node):
    def __init__(self, variable_type, identifier, value):
        self.type = variable_type
        self.identifier = identifier
        self.value = value

    # TODO
    def visit(self):
        return self.elements

    def __repr__(self):
        return f"[Declaration: {self.type}, {self.identifier}, {self.value}]"
