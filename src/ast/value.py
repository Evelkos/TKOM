# value.py

if __name__ == "__main__":
    from node import Node
else:
    from .node import Node

class Value(Node):
    def __init__(self, value):
        self.value = value

    # TODO
    def visit(self):
        return self.value

    def __repr__(self):
        return f"[Value: {self.value}]"