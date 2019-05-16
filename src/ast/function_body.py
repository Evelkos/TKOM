# function.py

from .node import Node


class FunctionBody(Node):
    def __init__(self, return_statement, content, line=None, column=None):
        self.line = line
        self.column = column
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