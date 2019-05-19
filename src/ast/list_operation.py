# list_operations.py

from .node import Node


class ListOperation(Node):
    def __init__(self, source_list, line=None, column=None):
        self.line = line
        self.column = column
        super().__init__()
        self.source_list = source_list

    def __repr__(self):
        return f"[ListOperation: {self.source_list}]"

    def accept(self, visitor):
        return visitor.visit_ListOperation(self)
        

class Filter(ListOperation):
    def __init__(self, source_list, conditions, line=None, column=None):
        self.line = line
        self.column = column
        self.source_list = source_list
        self.conditions = conditions

    def __eq__(self, other):
        return self.source_list == other.source_list and self.conditions == other.conditions

    def __repr__(self):
        return f"[Filter: {self.source_list}, {self.conditions}]"

    def accept(self, visitor):
        return visitor.visit_Filter(self)


class FilterCondition(Node):
    def __init__(self, operator, r_value, line=None, column=None):
        self.line = line
        self.column = column
        self.operator = operator
        self.r_value = r_value

    def __eq__(self, other):
        return self.operator == other.operator and self.r_value == other.r_value

    def __repr__(self):
        return f"[FilterCondition: {self.operator}, {self.r_value}]"

    def accept(self, visitor):
        return visitor.visit_FilterCondition(self)


class Each(ListOperation):
    def __init__(self, source_list, operator, expression, line=None, column=None):
        self.line = line
        self.column = column
        self.source_list = source_list
        self.operator = operator
        self.expression = expression

    def __eq__(self, other):
        return self.source_list == other.source_list and self.operator == other.operator and self.expression == other.expression

    def __repr__(self):
        return f"[Each: {self.source_list}, {self.operator}, {self.expression}]"

    def accept(self, visitor):
        return visitor.visit_Each(self)


class Get(ListOperation):
    def __init__(self, source_list, idx, line=None, column=None):
        self.line = line
        self.column = column
        self.source_list = source_list
        self.idx = idx

    def __eq__(self, other):
        return self.source_list == other.source_list and self.idx == other.idx

    def __repr__(self):
        return f"[Get: {self.source_list}, {self.idx}]"

    def accept(self, visitor):
        return visitor.visit_Get(self)


class Length(ListOperation):
    def __init__(self, source_list, line=None, column=None):
        self.line = line
        self.column = column
        self.source_list = source_list

    def __eq__(self, other):
        return self.source_list == other.source_list

    def __repr__(self):
        return f"[Length: {self.source_list}]"

    def accept(self, visitor):
        return visitor.visit_Length(self)


class Delete(ListOperation):
    def __init__(self, source_list, idx, line=None, column=None):
        self.line = line
        self.column = column
        self.source_list = source_list
        self.idx = idx

    def __eq__(self, other):
        return self.source_list == other.source_list and self.idx == other.idx

    def __repr__(self):
        return f"[Delete: {self.source_list}, {self.idx}]"

    def accept(self, visitor):
        return visitor.visit_Delete(self)