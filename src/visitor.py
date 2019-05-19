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
        self.map = []
        self.functions_def = []
        self.map.append({})

    def calculate_numeric_expression(self, left_operand, right_operand, operation):
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

    def calculate_list_expression(self, left_operand, right_operand, operation):
        if not (isinstance(left_operand, list) or (isinstance(right_operand, list))):
            return False

        if not isinstance(left_operand, list):
            left_operand = [left_operand]
        elif not isinstance(right_operand, list):
            right_operand = [right_operand]

        if operation == "+":
            return left_operand + right_operand
        # TODO - reszta operacji na listach


    def create_variable(self, variable_name, variable_value, variable_type):
        self.map[-1][variable_name] = {
            "type": variable_type,
            "value": None
        }
        self.save_variable(variable_name, variable_value)

    def get_map(self):
        return self.map

    def find_function_def(self, identifier):
        # TODO - nie moze byc dwoch roznych funkcji o tych samych nazwach!
        for function_def in self.functions_def:
            if functions_def.identifier == identifier:
                return function_def

    def is_variable_in_map(self, variable_name):
        return variable_name in self.map[-1]

    def is_value_type_correct(self, variable_value, variable_type):
        types_conversion = {
            "number": int,
            "list": list,
            "bool": bool
        }
        return variable_type in types_conversion and types_conversion[variable_type] == type(variable_value)

    def get_variable_value(self, variable_name):
        if self.is_variable_in_map(variable_name):
            return self.map[-1][variable_name]["value"]

    def save_variable(self, variable_name, variable_value):
        variable_type = self.map[-1][variable_name]["type"]
        if self.is_variable_in_map(variable_name):
            print(f"{variable_value}, {variable_type}")
            if self.is_value_type_correct(variable_value, variable_type):
                self.map[-1][variable_name]["value"] = variable_value
                return True
        else:
            print(f"nie ma zmiennej {variable_name} w mapie")
            return False

    def visit_Bool(self, node):
        if node.value == "true":
            return True
        elif node.value == "false":
            return False

    # z tego co widze, to to nie jest potrzebne, bo deklaracje zalatwia samo variable
    def visit_Declaration(self, node):
        return 0

    def visit_Expression(self, node):
        left_operand = node.left_operand.accept(self)
        operation = node.operation
        right_operand = node.right_operand.accept(self)

        # Przypisanie wartosci do zmiennej - przeniesc gdzies indziej
        if operation == "=":
            if isinstance(left_operand, str):
                right_operand_value = right_operand
                if isinstance(right_operand, str):
                    right_operand_value = self.get_variable_value(right_operand)
                self.save_variable(left_operand, right_operand_value)
                return
            else:
                raise Exception("TODO - przypisanie do R-wartosci!!! Wywalic blad")

        if isinstance(left_operand, str):
            left_operand = self.get_variable_value(left_operand)
        if isinstance(right_operand, str):
            right_operand = self.get_variable_value(right_operand)

        return_value = self.calculate_numeric_expression(left_operand, right_operand, operation)

        if return_value == None:
            return_value = self.calculate_list_expression(left_operand, right_operand, operation)
        return return_value
            

    def visit_Function(self, node):
        # TODO - zrobic zapisywanie argumentow do map! - chociaz nie, to lepiej zrobic w functionCall (chyba)
        # TODO - wszystkie argumenty funkcji zapisane pod nazwa funkcji?
        node.body.accept(self)
        print(self.map)
        return 0

    def visit_FunctionBody(self, node):
        for line in node.content:
            line.accept(self)

        # TODO - dorobic zwracanie odpowiedniej wartosci, czyli returna!!!
        # TODO - podzial na rozne typy zwracane - np. identyfikator da nam odczytana z map wartosc, a zwykla lista - liste
        return_statement = node.return_statement.accept(self)
        if isinstance(node.return_statement, Identifier): # TODO - zwrocenie zapisanej w map wartosci
            return_statement = self.get_variable_value(return_statement)
        return return_statement

    def visit_FunctionCall(self, node):
        # obliczenie wartosci argumentow wywolania
        arguments_value = []
        for argument in node.arguments:
            arguments_value.append(argument.accept(self))

        # odnalezienie definicji funkcji w postaci drzewa
        function_def = find_function_def(node.identifier)
        if function_def != None: # TODO - tak?
            function_def.accept(self)
        else:
            print(f"TODO wyjatek - nie znaleziono definicji funkcji {node.identifier.accept(self)}") # TODO - wyjatek

        # przygotowanie nowj, pustej pozycji w "mapie" (pustego slownika), zeby zmienne sie nie powtarzaly
        self.map.append({})

        # ustawienie zmiennych na stosie (mapie)
        for idx in function_def.arguments:
            function_def.arguments[idx].set_value(arguments_value[idx])
            function_def.arguments[idx].accept(self)
            function_def.arguments[idx].set_value(None)

        # TODO - jak zapisywac argumenty?
        # TODO - znalezc definicje funkcji, wyciagnac nazwy argumentow i wtedy je poprzydzielac?

        dictionary = {
            "name": node.identifier.accept(self),
            "arguments": "TODO"
        }
        self.map.append()
        return 0

    def visit_Identifier(self, node):
        return node.name

    def visit_List(self, node):
        return node.elements

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
        # TODO - jak z wyswietlaniem samych numerow i list?
        print(node.identifier)
        return 0

    def visit_Value(self, node):
        return node.value

    def visit_Variable(self, node):
        variable_name = node.identifier.accept(self)
        variable_type = node.type
        variable_value = node.value.accept(self)

        self.create_variable(variable_name, variable_value, variable_type)
        return 0

    def visit_VariableType(self, node):
        return 0

    def set_functions_def(self, functions_def):
        self.functions_def = functions_def