# list_condition.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "list_condition":
    from node import Node
else:
    from .node import Node


class ListCondition():
    def __init__(self, source_list, operation, result=None):
        self.list = source_list
        self.operation = operation
        self.result = result

    def visit(self):
        return self.elements

    def __repr__(self):
        return f"[ListOperation: {self.list}, {self.operation}, {self.result}]"
