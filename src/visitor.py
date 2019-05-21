# visitor.py
from .exceptions import UndefinedOperation, InvalidOperation, Undeclared, InvalidValue, DivisionError
from .ast.identifier import Identifier
from .ast.bool import Bool
from .ast.number import Number
from .ast.list import List
from .ast.expression import Expression
import operator


class Visitor:
    def __init__(self):
        self.map = []
        self.functions_def = []
        self.map.append({})

    @staticmethod
    def calculate_bool_expression(left_operand, right_operand, operation):
        if isinstance(left_operand, bool) and isinstance(right_operand, bool):
            if operation == "+":
                return left_operand or right_operand
            elif operation == "*":
                return left_operand and right_operand
            else:
                raise UndefinedOperation(type(left_operand).__name__, operation, type(left_operand).__name__)

    @staticmethod
    def calculate_list_expression(left_operand, right_operand, operation):
        if isinstance(left_operand, list) or (isinstance(right_operand, list)):
            if not isinstance(left_operand, list):
                left_operand = [left_operand]
            elif not isinstance(right_operand, list):
                right_operand = [right_operand]

            if operation == "+":
                return left_operand + right_operand
            else:
                raise UndefinedOperation(type(left_operand).__name__, operation, type(left_operand).__name__)

    @staticmethod
    def calculate_numeric_expression(left_operand, right_operand, operation):
        if isinstance(left_operand, int) and isinstance(right_operand, int):
            if operation == "+":
                return left_operand + right_operand
            elif operation == "-":
                return left_operand - right_operand
            elif operation == "*":
                return left_operand * right_operand
            elif operation == "/":
                if right_operand == 0:
                    raise DivisionError()
                return int(left_operand / right_operand)
            else:
                raise UndefinedOperation(type(left_operand).__name__, operation, type(left_operand).__name__)

    @staticmethod
    def convert_to_variable_object(value):
        if isinstance(value, int):
            return Number(value)
        elif isinstance(value, bool):
            return Bool(value)
        elif isinstance(value, list):
            return List(value)

    def create_variable(self, variable_name, variable_type):
        self.map[-1][variable_name] = {
            "type": variable_type,
            "value": None
        }

    def get_map(self):
        return self.map

    def get_variable_value(self, variable_name):
        if self.is_variable_in_map(variable_name):
            return self.map[-1][variable_name]["value"]
        else:
            raise Undeclared("variable", variable_name)
        
    def find_function_def(self, identifier, arguments_num):
        for function_def in self.functions_def:
            if function_def.identifier == identifier and len(function_def.arguments) == arguments_num:
                return function_def

    def is_variable_in_map(self, variable_name):
        return variable_name in self.map[-1]


    @staticmethod
    def is_value_type_correct(variable_value, variable_type):
        types_conversion = {
            "number": int,
            "list": list,
            "bool": bool
        }
        return variable_type in types_conversion and types_conversion[variable_type] == type(variable_value)

    def save_variable(self, variable_name, variable_value):
        if self.is_variable_in_map(variable_name):
            variable_type = self.map[-1][variable_name]["type"]
            if self.is_value_type_correct(variable_value, variable_type):
                self.map[-1][variable_name]["value"] = variable_value
                return True
            raise InvalidValue(variable_type, type(variable_value).__name__)
        raise Undeclared("variable", variable_name)

    def try_variable_assign(self, operation, left_operand, right_operand):
        if operation == "=":
            if isinstance(left_operand, str):
                right_operand_value = right_operand
                if isinstance(right_operand, str):
                    right_operand_value = self.get_variable_value(right_operand)
                self.save_variable(left_operand, right_operand_value)
                return True
            else:
                raise InvalidOperation("r-value", "=", "r-value")

    @staticmethod
    def visit_bool(node):
        if node.value == "true":
            return True
        elif node.value == "false":
            return False

    def visit_expression(self, node):
        left_operand = node.left_operand.accept(self)
        operation = node.operation
        right_operand = node.right_operand.accept(self)
        
        if self.try_variable_assign(operation, left_operand, right_operand):
            return

        if isinstance(left_operand, str):
            left_operand = self.get_variable_value(left_operand)
        if isinstance(right_operand, str):
            right_operand = self.get_variable_value(right_operand)

        return_value = self.calculate_bool_expression(left_operand, right_operand, operation)
        if return_value is None:
            return_value = self.calculate_numeric_expression(left_operand, right_operand, operation)
        if return_value is None:
            return_value = self.calculate_list_expression(left_operand, right_operand, operation)
        if return_value is None:
            raise UndefinedOperation(type(left_operand).__name__, operation, type(left_operand).__name__)
        return return_value

    def visit_function(self, node):
        if node.body is not None:
            return node.body.accept(self)

    def visit_function_body(self, node):
        for line in node.content:
            line.accept(self)
        return_statement = node.return_statement.accept(self)
        if isinstance(node.return_statement, Identifier):
            return_statement = self.get_variable_value(return_statement)
        return return_statement

    def visit_function_call(self, node):
        function_def = self.find_function_def(node.identifier, len(node.arguments))
        if function_def is not None:
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
        raise Undeclared("function", node.identifier.accept(self))

    @staticmethod
    def visit_identifier(node):
        return node.name

    def visit_list(self, node):
        elements = []
        for element in node.elements:
            elements.append(element.accept(self))
        return elements

    def is_element_meet_the_conditions(self, element, conditions):
        operators = {
            ">": operator.gt,
            "<": operator.lt,
            ">=": operator.ge,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne
        }
        for condition in conditions:
            operation, expression = condition.accept(self)
            operation = operators[operation]
            if not (operation(element, expression.accept(self))):
                return False
        return True

    def visit_filter(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)

        result_list = []
        for element in source_list:
            if self.is_element_meet_the_conditions(element, node.conditions):
                result_list.append(element)
        return result_list

    @staticmethod
    def visit_filter_condition(node):
        return node.operator, node.r_value

    def visit_each(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)

        new_list = []
        for list_element in source_list:
            left_operand = self.convert_to_variable_object(list_element)
            operation = node.operator
            right_operand = node.expression
            new_list.append((Expression(left_operand, operation, right_operand)).accept(self))
        return new_list

    def visit_get(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        position_to_get = node.idx.accept(self)
        if isinstance(position_to_get, str):
            position_to_get = self.get_variable_value(position_to_get)
        return source_list[position_to_get]

    def visit_length(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        return len(source_list)

    def visit_delete(self, node):
        source_list = node.source_list.accept(self)
        if isinstance(source_list, str):
            source_list = self.get_variable_value(source_list)
        position_to_delete = node.idx.accept(self)
        if isinstance(position_to_delete, str):
            position_to_delete = self.get_variable_value(position_to_delete)

        if position_to_delete in range(0, len(source_list)):
            source_list.pop(position_to_delete)
        return source_list

    @staticmethod
    def visit_number(node):
        return node.value

    def visit_print_function(self, node):
        result = node.identifier.accept(self)
        if isinstance(result, str):
            result = self.get_variable_value(result)
        print(result)

    @staticmethod
    def visit_value(node):
        return node.value

    def visit_variable(self, node):
        variable_name = node.identifier.accept(self)
        variable_type = node.type

        self.create_variable(variable_name, variable_type)

        if node.value is not None:
            variable_value = node.value.accept(self)
            self.save_variable(variable_name, variable_value)

    def set_functions_def(self, functions_def):
        self.functions_def = functions_def
        print(self.functions_def)
