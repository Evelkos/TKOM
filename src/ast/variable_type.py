# function.py
if __name__ == "__main__":
    from node import Node
else:
    from .node import Node


class VariableType(Node):
    def __init__(self, type_name):
        super().__init__()
        self.type = type_name

    # TODO
    def visit(self):
        return self.type

    def __repr__(self):
        return f"[Type: {self.type}]"