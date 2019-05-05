# parser.py


if __name__ == "__main__" or __name__ == "parser":
    from source import Source
    from token import Token, Type, Symbol
    from exceptions import InvalidSyntax
    from ast.function import Function
    from ast.identifier import Identifier
    from ast.variable import Variable
    from ast.variable_type import VariableType
    from ast.node import Node
    from ast.bool import Bool
    from ast.number import Number
    from ast.list import List
    from ast.function_body import FunctionBody
    from ast.function_call import FunctionCall
    from ast.print_function import PrintFunction
    from ast.declaration import Declaration
    from ast.expression import Expression
    from ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get, Length, Delete

else:
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


variable_types = [Type.LIST_TYPE, Type.NUMBER_TYPE, Type.BOOL_TYPE]


class Parser():
    def __init__(self, source, lexer):
        self.source = source
        self.lexer = lexer
        self.lexer.build_next_token()
        self.current_token = lexer.get_token()


    def check_type(self, token_type):
        if self.current_token.get_type() == token_type:
            return True
        return False


    def consume(self):
        self.current_token = self.get_next_token()


    def get_next_token(self):
        self.lexer.build_next_token()
        return self.lexer.get_token()


    def get_and_consume_token(self):
        token = self.current_token
        self.consume()
        return token


    def require_and_consume(self, token_type):
        token = self.require_token(token_type)
        self.consume()
        return token


    def require_and_consume_token_in_types(self, type_list):
        for token_type in type_list:
            if token_type == self.current_token.get_type():
                token = self.current_token
                self.consume()
                return token
        raise InvalidSyntax(
            f"On position {self.source.get_position()} "
            f"expected '{type_list}', "
            f"got {self.current_token.get_type()}: "
            f"{self.current_token.get_value()}"
        )

    def require_token(self, token_type):
        if self.current_token.get_type() == token_type:
            token = self.current_token
            return token
        else:
            raise InvalidSyntax(
                f"On position {self.source.get_position()} "
                f"expected '{token_type}', "
                f"got {self.current_token.get_type()}: "
                f"{self.current_token.get_value()}"
            )


    def parse(self):
        functions = []
        while self.current_token.get_type() != Type.EOF:
            function = self.parse_function()
            functions.append(function)
        return functions


    def parse_arguments(self):
        variable_types = [Type.LIST_TYPE, Type.NUMBER_TYPE, Type.BOOL_TYPE]
        arguments = []

        while self.current_token.get_type() in variable_types:
            variable_type = self.parse_type()
            variable_name = self.parse_identifier()
            arguments.append(Variable(variable_type, variable_name))
            if self.current_token.get_type() == Type.COMMA:
                self.consume()

        return arguments


    def parse_bool(self):
        token = self.require_and_consume(Type.BOOL)
        result_bool = Bool(token.get_value())
        return result_bool


    def parse_component(self):
        if self.check_type(Type.BOOL):
            return self.parse_bool()
        elif self.check_type(Type.NUMBER):
            return self.parse_number()
        elif self.check_type(Type.IDENTIFIER):
            identifier = self.parse_identifier()
            if self.check_type(Type.DOT):
                return self.parse_list_component(identifier)
            elif self.check_type(Type.OP_BRACKET):
                return self.parse_function_call(identifier)
            else:
                return identifier
        else:
            standard_list = self.parse_list()
            if self.check_type(Type.DOT):
                return self.parse_list_component(standard_list)
            else:
                return standard_list


    def parse_content(self):
        lines = []

        end_of_content_token_types = [Type.RETURN, Type.CL_CURLY_BRACKET]
        while self.current_token.get_type() not in end_of_content_token_types:
            line = self.parse_line()
            lines.append(line)

        return lines


    def parse_declaration(self):
        variable_type = self.parse_type()
        variable_identifier = self.parse_identifier()
        value = None

        if self.check_type(Type.ASSIGN):
            self.require_and_consume(Type.ASSIGN)
            value = self.parse_expression()

        declaration = Variable(variable_type, variable_identifier, value)

        return declaration


    def parse_elements(self, stop_type): # uzywane przy liscie: koniec ']' oraz funkcji: koniec ')'
        elements = []
        while self.current_token.get_type() != stop_type:
            if self.check_type(Type.BOOL):
                elements.append(self.parse_bool())
            elif self.check_type(Type.NUMBER):
                elements.append(self.parse_number())
            elif self.check_type(Type.IDENTIFIER):
                elements.append(self.parse_identifier())
            else:
                elements.append(self.parse_list())
            if self.check_type(Type.COMMA):
                self.consume()
        return elements


    def parse_expression(self):
        factor = self.parse_multiplication()

        if type(factor) == Identifier:
            if self.check_type(Type.ASSIGN):
                operator = self.get_and_consume_token().get_value()
                new_factor = self.parse_expression()
                return Expression(factor, operator, new_factor)          

        while self.check_type(Type.PLUS) or self.check_type(Type.MINUS):
            operator = self.get_and_consume_token()
            new_factor = self.parse_multiplication()
            factor = Expression(factor, operator.get_value(), new_factor)
        return factor


    def parse_factor(self):
        if self.check_type(Type.OP_BRACKET):
            self.require_and_consume(Type.OP_BRACKET)
            factor = self.parse_expression()
            self.require_and_consume(Type.CL_BRACKET)
        else:
            factor = self.parse_component()
        return factor


    def parse_function(self):
        self.require_and_consume(Type.FUNCTION)

        identifier = self.parse_identifier()

        self.require_and_consume(Type.OP_BRACKET)
        arguments = None
        if self.current_token.get_type() != Type.CL_BRACKET:
            arguments = self.parse_arguments()
        self.require_and_consume(Type.CL_BRACKET)

        self.require_and_consume(Type.OP_CURLY_BRACKET)
        body = None
        if self.current_token.get_type() != Type.CL_CURLY_BRACKET:
            body = self.parse_function_body()
        self.require_and_consume(Type.CL_CURLY_BRACKET)

        function = Function(identifier, arguments, body)
        return function


    def parse_function_body(self):
        end_of_content_token_types = [Type.RETURN, Type.CL_CURLY_BRACKET]
        content = None
        if self.current_token.get_type() not in end_of_content_token_types:
            content = self.parse_content()

        return_statement = None
        if self.current_token.get_type() == Type.RETURN:
            return_statement = self.parse_return()
            self.require_and_consume(Type.SEMICOLON)

        function_body = FunctionBody(return_statement, content)
        return function_body


    def parse_function_call(self, function_identifier):
        self.require_and_consume(Type.OP_BRACKET)
        arguments = self.parse_elements(Type.CL_BRACKET)
        self.require_and_consume(Type.CL_BRACKET)
        return FunctionCall(function_identifier, arguments)


    def parse_identifier(self):
        token = self.require_and_consume(Type.IDENTIFIER)
        identifier = Identifier(token.get_value())
        return identifier


    def parse_line(self):
        if self.current_token.get_type() == Type.PRINT:
            line = self.parse_print()
        elif self.current_token.get_type() in variable_types:
            line = self.parse_declaration()
        else:
            line = self.parse_expression()
        self.require_and_consume(Type.SEMICOLON)
        return line


    def parse_list(self):
        self.require_and_consume(Type.OP_SQUARE_BRACKET)
        elements = self.parse_elements(Type.CL_SQUARE_BRACKET)
        self.require_and_consume(Type.CL_SQUARE_BRACKET)
        return List(elements)


    def parse_list_component(self, tmp_list):
        while self.check_type(Type.DOT):
            tmp_list = self.parse_list_operation(tmp_list)
        return tmp_list


    def parse_list_operation(self, tmp_list):
        self.require_and_consume(Type.DOT)
        if self.check_type(Type.FILTER):
            return self.parse_list_operation_filter(tmp_list)
        elif self.check_type(Type.EACH):
            return self.parse_list_operation_each(tmp_list)
        elif self.check_type(Type.GET):
            return self.parse_list_operation_get(tmp_list)
        elif self.check_type(Type.LENGTH):
            return self.parse_list_operation_length(tmp_list)
        else:
            return self.parse_list_operation_delete(tmp_list)


    def parse_list_operation_delete(self, tmp_list):
        self.require_and_consume(Type.DELETE)
        self.require_and_consume(Type.OP_BRACKET)

        if self.check_type(Type.NUMBER):
            argument = self.parse_number()
        else:
            token = self.require_and_consume(Type.IDENTIFIER)
            argument = self.parse_identifier()

        self.require_and_consume(Type.CL_BRACKET)

        return Delete(tmp_list, number)


    def parse_list_operation_each(self, tmp_list):
        self.require_and_consume(Type.EACH)
        self.require_and_consume(Type.OP_BRACKET)

        operation = self.parse_operation()
        self.require_and_consume(Type.COMMA)
        standard_operation = self.parse_expression()

        self.require_and_consume(Type.CL_BRACKET)

        return Each(tmp_list, operation, standard_operation)


    def parse_list_operation_filter(self, tmp_list):
        self.require_and_consume(Type.FILTER)
        self.require_and_consume(Type.OP_BRACKET)
        
        single_condition = self.parse_single_condition()
        conditions = [single_condition]

        while self.check_type(Type.AND):
            self.require_and_consume(Type.AND)
            single_condition = self.parse_single_condition()
            conditions.append(single_condition)

        self.require_and_consume(Type.CL_BRACKET)

        return Filter(tmp_list, conditions)


    def parse_list_operation_get(self, tmp_list):
        self.require_and_consume(Type.GET)
        self.require_and_consume(Type.OP_BRACKET)

        if self.check_type(Type.NUMBER):
            argument = self.parse_number()
        else:
            token = self.require_and_consume(Type.IDENTIFIER)
            argument = self.parse_identifier()

        self.require_and_consume(Type.CL_BRACKET)

        return Get(tmp_list, argument)


    def parse_list_operation_length(self, tmp_list):
        self.require_and_consume(Type.LENGTH)
        self.require_and_consume(Type.OP_BRACKET)
        self.require_and_consume(Type.CL_BRACKET)
        return Length(tmp_list)


    def parse_multiplication(self):
        factor = self.parse_factor()
        while self.check_type(Type.STAR) or self.check_type(Type.DIVIDE):
            operator = self.get_and_consume_token().get_value()
            new_factor = self.parse_factor()
            factor = Expression(factor, operator, new_factor)
        return factor


    def parse_number(self):
        token = self.require_and_consume(Type.NUMBER)
        result_number = Number(token.get_value())
        return result_number


    def parse_operation(self):
        if self.check_type(Type.PLUS):
            return self.require_and_consume(Type.PLUS).get_value()
        elif self.check_type(Type.MINUS):
            return self.require_and_consume(Type.MINUS).get_value()
        elif self.check_type(Type.STAR):
            return self.require_and_consume(Type.STAR).get_value()
        else:
            return self.require_and_consume(Type.DIVIDE).get_value()


    def parse_print(self):
        self.require_and_consume(Type.PRINT)
        identifier = self.parse_identifier()
        return PrintFunction(identifier)


    def parse_return(self):
        self.require_and_consume(Type.RETURN)
        if self.current_token.get_type() == Type.BOOL:
            return self.parse_bool()
        elif self.current_token.get_type() == Type.NUMBER:
            return self.parse_number()
        elif self.current_token.get_type() == Type.IDENTIFIER:
            return self.parse_identifier()
        else:
            return self.parse_list()


    def parse_single_condition(self):
        if self.current_token.get_value() == "x":
            self.consume()

        possible_operators = [Type.LESS_THAN, Type.GREATER_THAN, Type.LESS_OR_EQUAL_TO, Type.GREATER_OR_EQUAL_TO, Type.EQUAL_TO, Type.NOT_EQUAL_TO]
        token = self.require_and_consume_token_in_types(possible_operators)
        operator = token.get_value()
        expression = self.parse_expression()
        return FilterCondition(operator, expression)


    def parse_type(self):
        token = self.require_and_consume_token_in_types(variable_types)
        return token.get_value()
        # if self.current_token.get_type() in variable_types:
        #     argument_type = VariableType(self.current_token.get_value())
        #     self.consume()
        # return argument_type
