# visitor.py
from .source import Source
from .token import Token, Type, Symbol
from .lexer import Lexer
from .exceptions import InvalidSyntax
from .ast.function import Function
from .ast.identifier import Identifier
from .ast.variable import Variable
from .ast.node import Node
from .ast.bool import Bool
from .ast.number import Number
from .ast.list import List
from .ast.function_body import FunctionBody
from .ast.function_call import FunctionCall
from .ast.print_function import PrintFunction
from .ast.expression import Expression
from .ast.list_operation import Filter, FilterCondition, Each, Get, Length, Delete
from .env.deep_chain_map import DeepChainMap



class Visitor():
    def __init__(self):
        self.map = []
        self.functions_def = []
        self.map.append({})

    def calculate_bool_expression(self, left_operand, right_operand, operation):
        if isinstance(left_operand, bool) and isinstance(right_operand, bool):
            if operation == "+":
                return left_operand or right_operand
            elif operation == "*":
                return left_operand and right_operand
            else:
                # TODO - dorobic obsluge bledow (nieznany operator)
                print("Nie zdefiniowano innych operacji dla bool")

    def calculate_list_expression(self, left_operand, right_operand, operation):
        if isinstance(left_operand, list) or (isinstance(right_operand, list)):
            if not isinstance(left_operand, list):
                left_operand = [left_operand]
            elif not isinstance(right_operand, list):
                right_operand = [right_operand]

            if operation == "+":
                return left_operand + right_operand
            else:
                # TODO - dorobic obsluge bledow (nieznany operator)
                print("Nie zdefiniowano innych operacji dla list")

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
                print("Nie zdefiniowano innych operacji dla number")

    def create_variable(self, variable_name, variable_type):
        self.map[-1][variable_name] = {
            "type": variable_type,
            "value": None
        }

    def get_map(self):
        return self.map

    def find_function_def(self, identifier, arguments_num):
        for function_def in self.functions_def:
            if function_def.identifier == identifier and len(function_def.arguments) == arguments_num:
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

        return_value = self.calculate_bool_expression(left_operand, right_operand, operation)
        if return_value == None:
            return_value = self.calculate_numeric_expression(left_operand, right_operand, operation)
        if return_value == None:
            return_value = self.calculate_list_expression(left_operand, right_operand, operation)
        return return_value
            

    def visit_Function(self, node):
        return node.body.accept(self)

    def visit_FunctionBody(self, node):
        for line in node.content:
            line.accept(self)
        return_statement = node.return_statement.accept(self)
        if isinstance(node.return_statement, Identifier):
            return_statement = self.get_variable_value(return_statement)
        return return_statement

    def visit_FunctionCall(self, node):
        function_def = self.find_function_def(node.identifier, len(node.arguments))
        if function_def != None:
            self.map.append({})

            arguments_value = []
            for argument in node.arguments:
                arguments_value.append(argument.accept(self))

            for argument in function_def.arguments:
                argument.accept(self)

            for i in range(0, len(arguments_value)):
                variable_name = function_def.arguments[i].identifier.accept(self)
                self.save_variable(variable_name, arguments_value[i])

            result = function_def.accept(self)
            self.map.pop()
            return result

        else:
            print(f"TODO wyjatek - nie znaleziono definicji funkcji {node.identifier.accept(self)}") # TODO - wyjatek
        return 0

    def visit_Identifier(self, node):
        return node.name

    def visit_List(self, node):
        elements = []
        for element in node.elements:
            elements.append(element.accept(self))
        return elements

    def visit_Filter(self, node):
        return 0

    def visit_FilterCondition(self, node):
        return 0

    def visit_Each(self, node):
        return 0

    def visit_Get(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        position_to_get = node.idx.accept(self)
        if isinstance(position_to_get, str):
            position_to_get = self.get_variable_value(position_to_get)
        return source_list[position_to_get]

    def visit_Length(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        return len(source_list)

    def visit_Delete(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        position_to_delete = node.idx.accept(self)
        if isinstance(position_to_delete, str):
            position_to_delete = self.get_variable_value(position_to_delete)

        if position_to_delete in range(0, len(source_list)):
            source_list.pop(position_to_delete)
        return source_list

    def visit_Number(self, node):
        return node.value

    def visit_PrintFunction(self, node):
        result = node.identifier.accept(self)
        if isinstance(result, str):
            result = self.get_variable_value(result)
        print(result)

    def visit_Value(self, node):
        return node.value

    def visit_Variable(self, node):
        variable_name = node.identifier.accept(self)
        variable_type = node.type

        self.create_variable(variable_name, variable_type)

        if node.value != None:
            variable_value = node.value.accept(self)
            self.save_variable(variable_name, variable_value)

    def set_functions_def(self, functions_def):
        self.functions_def = functions_def
        print(f"Oto moje funkcje w visitorze: {self.functions_def}")