# parser.py


if __name__ == "__main__":
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


class Parser():
    def __init__(self, source, lexer):
        self.source = source
        self.lexer = lexer
        self.lexer.build_next_token()
        self.current_token = lexer.get_token()


    def consume(self):
        self.current_token = self.get_next_token()


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


    def require_and_consume(self, token_type):
        token = self.require_token(token_type)
        self.consume()
        return token


    def get_next_token(self):
        self.lexer.build_next_token()
        return self.lexer.get_token()


    def parse(self):
        functions = []
        while self.current_token.get_type() != Type.EOF:
            function = self.parse_function()
            functions.append(function)
        return functions


    def parse_function(self):
        self.require_and_consume(Type.FUNCTION)

        identifier = self.parse_identifier()

        self.require_and_consume(Type.OP_BRACKET)
        arguments = self.parse_arguments()
        self.require_and_consume(Type.CL_BRACKET)

        self.require_and_consume(Type.OP_CURLY_BRACKET)
        body = self.parse_function_body()
        self.require_and_consume(Type.CL_CURLY_BRACKET)

        function = Function(identifier, arguments, body)
        return function


    def parse_identifier(self):
        token = self.require_and_consume(Type.IDENTIFIER)
        identifier = Identifier(token.get_value())
        return identifier


    def parse_arguments(self):
        variable_types = [Type.LIST_TYPE, Type.NUMBER_TYPE, Type.BOOL_TYPE]
        arguments = []


        while self.current_token.get_type() in variable_types:
            argument_type = self.parse_type()
            argument_name = self.parse_identifier()
            argument = Variable(argument_type, argument_name)
            arguments.append(argument)
            if self.current_token.get_type() == Type.COMMA:
                self.consume()

        return arguments


    def parse_type(self):
        variable_types = [Type.LIST_TYPE, Type.NUMBER_TYPE, Type.BOOL_TYPE]

        if self.current_token.get_type() in variable_types:
            argument_type = VariableType(self.current_token.get_value())
            self.consume()
        return argument_type


    def parse_function_body(self):
        return_statement = []
        while self.current_token.get_type() != Type.CL_CURLY_BRACKET and self.current_token.get_type() != Type.RETURN:
            continue

        return_statement = None
        content = None
        if self.current_token.get_type() == Type.RETURN:
            return_statement = self.parse_return()

        function_body = FunctionBody(return_statement, content)
        print(function_body)
        return function_body

    def parse_return(self):
        self.require_and_consume(Type.RETURN)
        if self.current_token.get_type() == Type.BOOL:
            return_statement = self.parse_bool()
            return return_statement
        elif self.current_token.get_type() == Type.NUMBER:
            return_statement = self.parse_number()
            return return_statement
        elif self.current_token.get_type() == Type.IDENTIFIER:
            return_statement = self.parse_identifier()
            return return_statement
        else:
            return_statement = self.parse_list()
            return return_statement


    def parse_bool(self):
        token = self.require_and_consume(Type.BOOL)
        result_bool = Bool(token.get_value())
        return result_bool

    def parse_number(self):
        token = self.require_and_consume(Type.NUMBER)
        result_number = Number(token.get_value())
        return result_number


    def parse_list(self):
        self.require_and_consume(Type.OP_SQUARE_BRACKET)

        elements = []
        while self.current_token.get_type() != Type.CL_SQUARE_BRACKET:
            if self.current_token.get_type() == Type.BOOL:
                element = self.parse_bool()
            elif self.current_token.get_type() == Type.NUMBER:
                element = self.parse_number()
            elif self.current_token.get_type() == Type.IDENTIFIER:
                element = self.parse_identifier()
            else:
                element = self.parse_list()
            elements.append(element)
            if self.current_token.get_type() == Type.COMMA:
                self.consume()

        self.require_and_consume(Type.CL_SQUARE_BRACKET)
        return_list = List(elements)
        return return_list