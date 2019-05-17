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
from .env.deep_chain_map import DeepChainMap



class Visitor():
    def __init__(self):
        self.map = DeepChainMap()

    def get_map(self):
        return self.map

    def visit_Bool(self, node):
        return 0

    def visit_Declaration(self, node):
        return 0

    def visit_Expression(self, node):
        left_operand = node.left_operand.accept(self)
        operation = node.operation
        right_operand = node.right_operand.accept(self)

        if isinstance(left_operand, int) and isinstance(right_operand, int):
            if operation == "+":
                return left_operand + right_operand
            elif operation == "-":
                return left_operand - right_operand
            elif operation == "*":
                return left_operand * right_operand
            elif operation == "/":
                return (int)(left_operand / right_operand)
            else:
                # TODO - dorobic obsluge bledow (nieznany operator)
                print("Error w visit_Expression - nieznany operator dla numerow")

    def visit_Function(self, node):
        # TODO - zrobic zapisywanie argumentow do map!
        # TODO - wszystkie argumenty funkcji zapisane pod nazwa funkcji?
        node.body.accept(self)
        return 0

    def visit_FunctionBody(self, node):
        for line in node.content:
            line.accept(self)

        # TODO - dorobic zwracanie odpowiedniej wartosci, czyli returna!!!
        # TODO - podzial na rozne typy zwracane - np. identyfikator da nam odczytana z map wartosc, a zwykla lista - liste
        return_statement = node.return_statement.accept(self)
        if isinstance(node.return_statement, Identifier): # TODO - zwrocenie zapisanej w map wartosci
            print("TODO") # return odczytana_z_map_wartosc
        return return_statement

    def visit_FunctionCall(self, node):
        return 0

    def visit_Identifier(self, node):
        return node.name

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
        return node.value

    def visit_PrintFunction(self, node):
        return 0

    def visit_Value(self, node):
        return node.value

    def visit_Variable(self, node):
        variable_name = node.identifier.accept(self)
        variable_type = node.type
        variavle_value = node.value.accept(self)

        # TODO - dorobic zapisywanie zmiennej w ODPOWIEDNIM miejscu (w funkcji, czy cos)
        self.map[f"{variable_name}"] = {"type": variable_type, "value": variavle_value}

        # TODO - dorobic odpowiedni return (jeszcze nie wiem jaki)
        return 0

    def visit_VariableType(self, node):
        return 0