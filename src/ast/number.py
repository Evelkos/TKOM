# number.py
if __name__ == "__main__":
    from node import Node
    from value import Value
else:
    from .node import Node
    from .value import Value

class Number(Value):
    def __init__(self, value):
        self.value = int(value)

    # TODO
    def visit(self):
        super().visit()

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"[NUMBER: {self.value}]"