# function.py
if __name__ == "__main__":
    from node import Node
elif __name__ == "function":
    from node import Node
else:
    from .node import Node


class Function(Node):
    def __init__(self, function_identifier, arguments, body):
        super().__init__()
        self.identifier = function_identifier
        self.arguments = arguments
        self.body = body

    # TODO
    def visit(self):
        return self.identifier

    def __repr__(self):
        return f"[Function: {self.identifier}, {self.arguments}, {self.body}]"