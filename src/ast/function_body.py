# function.py
if __name__ == "__main__":
    from node import Node
else:
    from .node import Node


class FunctionBody(Node):
    def __init__(self, return_statement, content):
        super().__init__()
        self.return_statement = return_statement
        self.content = content

    def __eq__(self, other):
        return self.return_statement == other.return_statement and self.content == other.content

    def __repr__(self):
        return f"[FunctionBody: {self.return_statement}, {self.content}]"

    # TODO
    def visit(self):
        return self.return_statement