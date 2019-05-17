# visitor.py
from .source import Source
from .token import Token, Type, Symbol
from .lexer import Lexer
from .exceptions import InvalidSyntax
from .ast.function import Function
from .ast.identifier import Identifier
from .ast.variable import Variable
from .ast.variable_type import VariableType
from .ast.node import Node
from .ast.bool import Bool
from .ast.number import Number
from .ast.list import List
from .ast.function_body import FunctionBody
from .ast.function_call import FunctionCall
from .ast.print_function import PrintFunction
from .ast.declaration import Declaration
from .ast.expression import Expression
from .ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get, Length, Delete

class Visitor():
    def visit_Bool(self, node):
        return 0

    def visit_Declaration(self, node):
        return 0

    def visit_Expression(self, node):
        return 0

    def visit_Function(self, node):
        return 0

    def visit_FunctionBody(self, node):
        return 0

    def visit_FunctionCall(self, node):
        return 0

    def visit_Identifier(self, node):
        return 0

    def visit_List(self, node):
        return 0

    def visit_ListOperation(self, node):
        return 0

    def visit_Filter(self, node):
        return 0

    def visit_FilterCondition(self, node):
        return 0

    def visit_Each(self, node):
        return 0

    def visit_Get(self, node):
        return 0

    def visit_Length(self, node):
        return 0

    def visit_Delete(self, node):
        return 0

    def visit_Number(self, node):
        return 0

    def visit_PrintFunction(self, node):
        return 0

    def visit_Value(self, node):
        return 0

    def visit_Variable(self, node):
        return 0

    def visit_VariableType(self, node):
        return 0