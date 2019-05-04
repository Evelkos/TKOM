# number.py
if __name__ == "__main__":
    from node import Node
    from value import Value
elif __name__ == "bool":
    from node import Node
    from value import Value
else:
    from .node import Node
    from .value import Value

class Number(Value):
    def __init__(self, value):
        super().__init__(value)

    # TODO
    def visit(self):
        super().visit()

    def __repr__(self):
        return f"[NUMBER: {self.value}]"