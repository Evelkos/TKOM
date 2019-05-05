# variable.py
if __name__ == "__main__":
    from node import Node
elif __name__ == "variable":
    from node import Node
else:
    from .node import Node


class Variable(Node):
    def __init__(self, variable_type, variable_identifier, value=None):
        super().__init__()
        self.type = variable_type
        self.identifier = variable_identifier
        self.value = value

    # TODO
    def visit(self):
        return self.name

    def __repr__(self):
        return f"[Variable: {self.type}, {self.identifier}, {self.value}]"