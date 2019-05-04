# list_operations.py

if __name__ == "__main__":
    from node import Node
elif __name__ == "list_operation":
    from node import Node
else:
    from .node import Node


class ListOperation(Node):
    def __init__(self, source_list, operation):
        self.list = source_list
        self.operation = operation

    def visit(self):
        return self.list

    def __repr__(self):
        return f"[ListOperation: {self.list}, {self.operation}]"


class Filter(ListOperation):
    def __init__(self, source_list, operation):
        super().__init__(source_list, operation)
        self.condition

    def visit(self):
        return self.list

    def __repr__(self):
        return f"[Filter: {self.list}, {self.operation}, {self.condition}]"


class FilterCondition(Node):
    def __init__(self, operator, r_value):
        self.operator = operator
        self.r_value = r_value

    def visit(self):
        return self.operator, self.r_value

    def __repr__(self):
        return f"[FilterCondition: {self.operator}, {self.r_value}]"


class Each(ListOperation):
    def __init__(self, operation, standard_operation):
        self.operation = operation
        self.operation = standard_operation

    def visit(self):
        return self.operation

    def __repr__(self):
        return f"[Each: {self.operation}, {self.standard_operation}]"


class Get(ListOperation):
    def __init__(self, idx):
        self.idx = idx

    def visit(self):
        return self.idx

    def __repr__(self):
        return f"[Each: {self.idx}]"
