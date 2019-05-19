# list_operations.py

from .node import Node


class ListOperation(Node):
    def __init__(self, source_list, line=None, column=None):
        super().__init__(line, column)
        self.source_list = source_list
        # self.line = line
        # self.column = column

    def __repr__(self):
        pass

    def accept(self, visitor):
        pass
        

class Filter(ListOperation):
    def __init__(self, source_list, conditions, line=None, column=None):
        super().__init__(source_list, line, column)
        self.source_list = source_list
        self.conditions = conditions
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Filter) and self.source_list == other.source_list and self.conditions == other.conditions

    def __repr__(self):
        return f"[Filter: {self.source_list}, {self.conditions}]"

    def accept(self, visitor):
        return visitor.visit_filter(self)


class FilterCondition(Node):
    def __init__(self, operator, r_value, line=None, column=None):
        super().__init__(line, column)
        self.operator = operator
        self.r_value = r_value
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, FilterCondition) and self.operator == other.operator and self.r_value == other.r_value

    def __repr__(self):
        return f"[FilterCondition: {self.operator}, {self.r_value}]"

    def accept(self, visitor):
        return visitor.visit_filter_condition(self)


class Each(ListOperation):
    def __init__(self, source_list, operator, expression, line=None, column=None):
        super().__init__(source_list, line, column)
        self.source_list = source_list
        self.operator = operator
        self.expression = expression
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Each) and self.source_list == other.source_list and self.operator == other.operator and self.expression == other.expression

    def __repr__(self):
        return f"[Each: {self.source_list}, {self.operator}, {self.expression}]"

    def accept(self, visitor):
        return visitor.visit_each(self)


class Get(ListOperation):
    def __init__(self, source_list, idx, line=None, column=None):
        super().__init__(source_list, line, column)
        self.source_list = source_list
        self.idx = idx
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Get) and self.source_list == other.source_list and self.idx == other.idx

    def __repr__(self):
        return f"[Get: {self.source_list}, {self.idx}]"

    def accept(self, visitor):
        return visitor.visit_get(self)


class Length(ListOperation):
    def __init__(self, source_list, line=None, column=None):
        super().__init__(source_list, line, column)
        self.source_list = source_list
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Length) and self.source_list == other.source_list

    def __repr__(self):
        return f"[Length: {self.source_list}]"

    def accept(self, visitor):
        return visitor.visit_length(self)


class Delete(ListOperation):
    def __init__(self, source_list, idx, line=None, column=None):
        super().__init__(source_list, line, column)
        self.source_list = source_list
        self.idx = idx
        # self.line = line
        # self.column = column

    def __eq__(self, other):
        return isinstance(other, Delete) and self.source_list == other.source_list and self.idx == other.idx

    def __repr__(self):
        return f"[Delete: {self.source_list}, {self.idx}]"

    def accept(self, visitor):
        return visitor.visit_delete(self)
