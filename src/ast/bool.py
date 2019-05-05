# bool.py
if __name__ == "__main__":
    from node import Node
    from value import Value
elif __name__ == "bool":
    from node import Node
    from value import Value
else:
    from .node import Node
    from .value import Value

class Bool(Value):
    def __init__(self, value):
        super().__init__(value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"[BOOL: {self.value}]"

    # TODO
    def visit(self):
        super().visit()
