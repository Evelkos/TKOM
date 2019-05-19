# function.py

from .node import Node


class FunctionBody(Node):
    def __init__(self, return_statement, content, line=None, column=None):
        super().__init__(line, column)
        self.return_statement = return_statement
        self.content = content
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return (
                isinstance(other, FunctionBody) and
                self.return_statement == other.return_statement and
                self.content == other.content
        )

    def __repr__(self):
        return f"[FunctionBody: {self.return_statement}, {self.content}]"

    def accept(self, visitor):
        return visitor.visit_function_body(self)
