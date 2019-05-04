# function.py
if __name__ == "__main__":
    from node import Node
elif __name__ == "function":
    from node import Node
else:
    from .node import Node


class FunctionBody(Node):
    def __init__(self, return_statement, content):
        super().__init__()
        self.return_statement = return_statement
        self.content = content

    # TODO
    def visit(self):
        return self.return_statement

    def __repr__(self):
        return f"[FunctionBody: {self.return_statement}, {self.content}]"