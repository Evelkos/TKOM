# function.py
if __name__ == "__main__":
    from node import Node
    from identifier import identifier
elif __name__ == "function":
    from node import Node
    from identifier import Identifier
else:
    from .node import Node
    from .identifier import Identifier


class Function(Node):
    def __init__(self, function_identifier, arguments, body):
        self.identifier = function_identifier
        self.arguments = arguments
        self.body = body

    # TODO
    def visit():
        return self.identifier

    def __repr__(self):
        return f"[Function: {self.identifier}, {self.arguments}]"