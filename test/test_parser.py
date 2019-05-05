# from TKOM.src.parser import Parser
# from TKOM.src.lexer import Lexer
# from TKOM.src.source import Source
# from TKOM.src.exceptions import InvalidSyntax
# from TKOM.src.ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get, Length, Delete
# from TKOM.src.ast.number import Number
# from TKOM.src.ast.expression import Expression


from TKOM.src.parser import Parser
from TKOM.src.source import Source
from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
from TKOM.src.token import Token, Type, Symbol
from TKOM.src.exceptions import InvalidSyntax
from TKOM.src.ast.function import Function
from TKOM.src.ast.identifier import Identifier
from TKOM.src.ast.variable import Variable
from TKOM.src.ast.variable_type import VariableType
from TKOM.src.ast.node import Node
from TKOM.src.ast.bool import Bool
from TKOM.src.ast.number import Number
from TKOM.src.ast.list import List
from TKOM.src.ast.function_body import FunctionBody
from TKOM.src.ast.function_call import FunctionCall
from TKOM.src.ast.print_function import PrintFunction
from TKOM.src.ast.declaration import Declaration
from TKOM.src.ast.expression import Expression
from TKOM.src.ast.list_operation import ListOperation, Filter, FilterCondition, Each, Get, Length, Delete


import io
import pytest
import sys

def test_parse_number():
    sys.stdin = io.StringIO("1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_number() == Number(1)


def test_parse_component():
    sys.stdin = io.StringIO("1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Number(1)


def test_parse_number_with_number():
    sys.stdin = io.StringIO("123")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_number() == Number(123)


def test_parse_list_operation_get():
    sys.stdin = io.StringIO("get(1)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_get(tmp_list) == Get(tmp_list, Number(1))


def test_parse_list_operation_get_with_lists_with_different_length():
    sys.stdin = io.StringIO("get(1)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    assert parser.parse_list_operation_get(list_1) != Get(list_2, Number(2))


def test_parse_list_operation_get_with_different_possition():
    sys.stdin = io.StringIO("get(1)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_get(tmp_list) != Get(tmp_list, Number(2))


def test_parse_list_operation_length_with_lists_with_equal_length():
    sys.stdin = io.StringIO("length()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]

    assert parser.parse_list_operation_length(list_1) == Length(list_2)


def test_parse_list_operation_length_with_lists_with_different_length():
    sys.stdin = io.StringIO("length()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6, 7]
    assert parser.parse_list_operation_length(list_1) != Length(list_2)


def test_parse_multiplication_with_star():
    sys.stdin = io.StringIO("1 * 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Expression(Number(1), "*", Number(2))


def test_parse_multiplication_with_star_and_identifiers():
    sys.stdin = io.StringIO("abc * def")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Expression(Identifier("abc"), "*", Identifier("def"))


def test_parse_multiplication_with_divide():
    sys.stdin = io.StringIO("1 / 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Expression(Number(1), "/", Number(2))


def test_parse_multiplication_with_divide_and_identifiers():
    sys.stdin = io.StringIO("abc / def")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Expression(Identifier("abc"), "/", Identifier("def"))


def test_parse_multiplication_with_plus():
    sys.stdin = io.StringIO("1 + 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Number(1)


def test_parse_multiplication_with_minus():
    sys.stdin = io.StringIO("1 - 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Number(1)


def test_parse_multiplication_with_letter():
    sys.stdin = io.StringIO("1 a 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_multiplication() == Number(1)


def test_parse_multiplication_with_complex_example():
    sys.stdin = io.StringIO("abc * def / 123 + 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    first_expression = Expression(Identifier("abc"), "*", Identifier("def"))
    assert parser.parse_multiplication() == Expression(first_expression, "/", Number(123))


def test_parse_operation_with_plus():
    sys.stdin = io.StringIO("+")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_operation() == "+"


def test_parse_operation_with_minus():
    sys.stdin = io.StringIO("-")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_operation() == "-"


def test_parse_operation_with_star():
    sys.stdin = io.StringIO("*")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_operation() == "*"


def test_parse_operation_with_divide():
    sys.stdin = io.StringIO("/")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_operation() == "/"


def test_parse_print():
    sys.stdin = io.StringIO("print abc")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_print() == PrintFunction(Identifier("abc"))


def test_parse_return_with_false():
    sys.stdin = io.StringIO("return false")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_return() == Bool("false")


def test_parse_return_with_true():
    sys.stdin = io.StringIO("return true")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_return() == Bool("true")


def test_parse_return_with_number():
    sys.stdin = io.StringIO("return 123")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_return() == Number(123)


def test_parse_return_with_identifier():
    sys.stdin = io.StringIO("return identifier")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_return() == Identifier("identifier")


def test_parse_return_with_list():
    sys.stdin = io.StringIO("return [1, 2, 3]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    elements = [Number(1), Number(2), Number(3)]
    # result_list = List()

    assert parser.parse_return() == List(elements)


def test_parse_single_condition_with_GREATER_THAN():
    sys.stdin = io.StringIO("x > 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition(">", Number(1))


def test_parse_single_condition_with_LESS_THAN():
    sys.stdin = io.StringIO("x < 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition("<", Number(1))


def test_parse_single_condition_with_GREATER_OR_EQUAL_TO():
    sys.stdin = io.StringIO("x <= 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition("<=", Number(1))


def test_parse_single_condition_with_LESS_OR_EQUAL_TO():
    sys.stdin = io.StringIO("x <= 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition("<=", Number(1))


def test_parse_single_condition_with_EQUAL_TO():
    sys.stdin = io.StringIO("x == 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition("==", Number(1))


def test_parse_single_condition_with_NOT_EQUAL_TO():
    sys.stdin = io.StringIO("x != 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_single_condition() == FilterCondition("!=", Number(1))


# def test_parse_single_condition_with_complex_condition():
#     sys.stdin = io.StringIO("x > 1 + 2")
#     source = Source()
#     lexer = Lexer(source)
#     parser = Parser(source, lexer)

#     assert parser.parse_single_condition() == FilterCondition(">", Expression(Number(1), '+', Number(2)))


def test_parse_type_with_bool():
    sys.stdin = io.StringIO("bool")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    assert parser.parse_type() == "bool"


def test_parse_type_with_list():
    sys.stdin = io.StringIO("list")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    assert parser.parse_type() == "list"


def test_parse_type_with_number():
    sys.stdin = io.StringIO("number")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    assert parser.parse_type() == "number"


def test_parse_type_with_other_value():
    sys.stdin = io.StringIO("other")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    with pytest.raises(InvalidSyntax):
        parser.parse_type()
