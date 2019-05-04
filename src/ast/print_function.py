if __name__ == "__main__":
    from node import Node
elif __name__ == "print_function":
    from node import Node
else:
    from .node import Node

class PrintFunction(Node):
    def __init__(self, identifier):
        self.identifier = identifier

    # TODO
    def visit(self):
        return self.identifier

    def __repr__(self):
        return f"[PRINT: {self.identifier}]"
