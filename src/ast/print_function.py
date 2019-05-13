if __name__ == "__main__":
    from node import Node
else:
    from .node import Node

class PrintFunction(Node):
    def __init__(self, identifier):
        self.identifier = identifier

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __repr__(self):
        return f"[PRINT: {self.identifier}]"

    # TODO
    def visit(self):
        return self.identifier
