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
    from ast.print_function import PrintFunction
    from ast.declaration import Declaration
    from ast.expression import Expression
    from ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get

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
    from .ast.print_function import PrintFunction
    from .ast.declaration import Declaration
    from .ast.expression import Expression
    from .ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get


variable_types = [Type.LIST_TYPE, Type.NUMBER_TYPE, Type.BOOL_TYPE]


class Parser():
    def __init__(self, source, lexer):
        self.source = source
        self.lexer = lexer
        self.lexer.build_next_token()
        self.current_token = lexer.get_token()


    def consume(self):
        print(self.current_token)
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

    def check_type(self, token_type):
        if self.current_token.get_type() == token_type:
            return True
        return False

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
        if self.current_token.get_type() != Type.CL_BRACKET:
            arguments = self.parse_arguments()
        else:
            arguments = None
        self.require_and_consume(Type.CL_BRACKET)

        self.require_and_consume(Type.OP_CURLY_BRACKET)
        if self.current_token.get_type() != Type.CL_CURLY_BRACKET:
            body = self.parse_function_body()
        else:
            body = None
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
        if self.current_token.get_type() in variable_types:
            argument_type = VariableType(self.current_token.get_value())
            self.consume()
        return argument_type


    def parse_function_body(self):
        end_of_content_token_types = [Type.RETURN, Type.CL_CURLY_BRACKET]
        if self.current_token.get_type() not in end_of_content_token_types:
            content = self.parse_content()
        else:
            content = None

        if self.current_token.get_type() == Type.RETURN:
            return_statement = self.parse_return()
        else:
            return_statement = None

        function_body = FunctionBody(return_statement, content)
        return function_body


    def parse_content(self):
        lines = []

        end_of_content_token_types = [Type.RETURN, Type.CL_CURLY_BRACKET]
        while self.current_token.get_type() not in end_of_content_token_types:
            line = self.parse_line()
            lines.append(line)

        return lines


    def parse_line(self):
        line = None
        if self.current_token.get_type() == Type.PRINT:
            line = self.parse_print()
        if self.current_token.get_type() in variable_types:
            line = self.parse_declaration()
        self.require_and_consume(Type.SEMICOLON)
        return line


    def parse_print(self):
        self.require_and_consume(Type.PRINT)
        identifier = self.parse_identifier()
        print_node = PrintFunction(identifier)
        return print_node


    def parse_declaration(self):
        variable_type = self.parse_type()
        variable_identifier = self.parse_identifier()

        if self.check_type(Type.ASSIGN):
            self.require_and_consume(Type.ASSIGN)
            value = self.parse_standard_operation()

        declaration = Variable(variable_type, variable_identifier)


    def parse_standard_operation(self):
        # component[operator component]* | '('component[operator component]*')'
        if self.check_type(Type.OP_BRACKET):
            self.require_and_consume(Type.OP_BRACKET)

        component = self.parse_component()

        operation_types = [Type.PLUS, Type.MINUS, Type.STAR, Type.DIVIDE]

        if self.current_token.get_type() in operation_types:
            operation = self.parse_operation()
            expression = Expression(component, operation, self.parse_standard_operation())
        else:
            expression = component

        if self.check_type(Type.CL_BRACKET):
            self.require_and_consume(Type.CL_BRACKET)

        return expression


    def parse_component(self):
        if self.check_type(Type.BOOL):
            return_statement = self.parse_bool()
        elif self.check_type(Type.NUMBER):
            return_statement = self.parse_number()
        elif self.check_type(Type.IDENTIFIER):
            return_statement = self.parse_identifier()
            if self.check_type(Type.DOT):
                return_statement = self.parse_list_operation(return_statement)
                print("TODO - list operation")
                parse_list_operation()
            elif self.check_type(Type.OP_BRACKET):
                print("TODO - function call")
        else:
            return_statement = self.parse_list()
            if self.check_type(Type.DOT):
                print("TODO - list operation")
                parse_list_operation()


    def parse_list_operation(self, tmp_list):
        self.require_and_consume(Type.DOT)
        if self.check_type(Type.FILTER):
            node = self.parse_list_operation_filter()
        elif self.check_type(Type.EACH):
            node = self.parse_list_operation_each()
        elif self.check_type(Type.GET):
            token = self.require_and_consume(Type.GET)
            print("TODO - get")
        elif self.check_type(Type.LENGTH):
            token = self.require_and_consume(Type.LENGTH)
            print("TODO - lenght")
        else:
            token = self.require_and_consume(Type.DELETE)
            print("TODO - delete")


    def parse_list_operation_filter(self):
        self.require_and_consume(Type.FILTER)
        self.require_and_consume(Type.OP_BRACKET)

        conditions = []
        
        single_condition = parse_single_condition()
        conditions.append(single_condition)

        while self.check_type(Type.AND):
            single_condition = parse_single_condition()
            conditions.append(single_condition)

        self.require_and_consume(Type.CL_BRACKET)

        filter_operation = Filter(tmp_list, conditions)
        return filter_operation


    def parse_single_condition(self):
        if self.current_token.get_value() == "x":
            self.consume()

        possible_operators = [Type.LESS_THAN, Type.GREATER_THAN, LESS_OR_EQUAL_TO, GREATER_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO]
        if self.current_token.get_type() in possible_operators:
            token = self.current_token
            self.consume()
            argument = self.parse_component()
            filter_condition = FilterCondition(token.value(), argument)
            return filter_condition
        else:
            raise InvalidSyntax(
                f"On position {self.source.get_position()} "
                f"expected '{possible_operators}', "
                f"got {self.current_token.get_type()}: "
                f"{self.current_token.get_value()}"
            )


    def parse_list_operation_each(self):
        self.require_and_consume(Type.EACH)
        self.require_and_consume(Type.OP_BRACKET)

        operation = self.parse_operation()
        standard_operation = self.parse_standard_operation()

        self.require_and_consume(Type.CL_BRACKET)

        each_operation = Each(operation, standard_operation)
        return each_operation


    def parse_operation(self):
        if self.check_type(Type.PLUS):
            operation = Type.PLUS
        if self.check_type(Type.MINUS):
            operation = Type.MINUS
        if self.check_type(Type.STAR):
            operation = Type.STAR
        if else::
            operation = Type.DIVIDE

        self.consume()
        return operation


    def parse_return(self):
        self.require_and_consume(Type.RETURN)
        if self.current_token.get_type() == Type.BOOL:
            return_statement = self.parse_bool()
        elif self.current_token.get_type() == Type.NUMBER:
            return_statement = self.parse_number()
        elif self.current_token.get_type() == Type.IDENTIFIER:
            return_statement = self.parse_identifier()
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