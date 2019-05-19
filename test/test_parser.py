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

def test_parse():
    sys.stdin = io.StringIO(
        "function name1(bool a, number b) {"
        "    return [abc, 123, [345, xyz]];"
        "}"
        "function name2(list abc) {"
        "    number a = abc.get(2);"
        "    print abc;"
        "    abc.each(*, 564).length();"
        "    a = 2 + 2;"
        "    return 0;"
        "    # comment \n"
        "}"
    )
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    arguments_1 = [Variable("bool", Identifier("a")), Variable("number", Identifier("b"))]
    function_body_1 = FunctionBody(List([Identifier("abc"), Number(123), List([Number(345), Identifier("xyz")])]), [])
    fun_1 = Function(Identifier("name1"), arguments_1, function_body_1)

    arguments_2 = [Variable("list", Identifier("abc"))]
    line_1 = Variable("number", Identifier("a"), Get(Identifier("abc"), Number(2)))
    line_2 = PrintFunction(Identifier("abc"))
    line_3 = Length(Each(Identifier("abc"), "*", Number(564)))
    line_4 = Expression(Identifier("a"), "=", Expression(Number(2), "+", Number(2)))
    function_body_2 = FunctionBody(Number(0), [line_1, line_2, line_3, line_4])
    fun_2 = Function(Identifier("name2"), arguments_2, function_body_2)
    assert parser.parse() == [fun_1, fun_2]


def test_parse_arguments():
    sys.stdin = io.StringIO("bool a, list b, number c")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    var_1 = Variable("bool", Identifier("a"), None)
    var_2 = Variable("list", Identifier("b"), None)
    var_3 = Variable("number", Identifier("c"), None)
    assert parser.parse_arguments() == [var_1, var_2, var_3]


def test_parse_bool_with_true():
    sys.stdin = io.StringIO("true")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_bool() == Bool("true")


def test_parse_bool_with_false():
    sys.stdin = io.StringIO("false")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_bool() == Bool("false")



def test_parse_component_with_number():
    sys.stdin = io.StringIO("987654321")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Number(987654321)


def test_parse_component_with_identifier():
    sys.stdin = io.StringIO("iDeNtIfIeR")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Identifier("iDeNtIfIeR")


def test_parse_component_with_list():
    sys.stdin = io.StringIO("[987, abc, [321, xyz]]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == List([Number(987), Identifier("abc"), List([Number(321), Identifier("xyz")])])


def test_parse_component_with_true():
    sys.stdin = io.StringIO("true")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Bool("true")


def test_parse_component_with_false():
    sys.stdin = io.StringIO("false")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Bool("false")


def test_parse_component_with_function_call():
    sys.stdin = io.StringIO("fun()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == FunctionCall(Identifier("fun"), [])


def test_parse_component_with_list_operation_get():
    sys.stdin = io.StringIO("myList.get(9987231)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Get(Identifier("myList"), Number(9987231))


def test_parse_component_with_list_operation_delete():
    sys.stdin = io.StringIO("[1, 2, 3].delete(3)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_component() == Delete(List([Number(1), Number(2), Number(3)]), Number(3))


def test_parse_content_with_bracket():
    sys.stdin = io.StringIO("x = 3; bool y = 4;}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    line_1 = Expression(Identifier("x"), "=", Number(3))
    line_2 = Variable("bool", Identifier("y"), Number(4))

    assert parser.parse_content() == [line_1, line_2]


def test_parse_content_with_return():
    sys.stdin = io.StringIO("xyz = 3; bool dfdf = 4; return 1")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    line_1 = Expression(Identifier("xyz"), "=", Number(3))
    line_2 = Variable("bool", Identifier("dfdf"), Number(4))

    assert parser.parse_content() == [line_1, line_2]


def test_parse_declaration_without_assign():
    sys.stdin = io.StringIO("bool a;")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_declaration() == Variable("bool", Identifier("a"))


def test_parse_declaration_with_assign():
    sys.stdin = io.StringIO("bool a = [i];")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_declaration() == Variable("bool", Identifier("a"), List([Identifier("i")]))


def test_parse_number_with_number():
    sys.stdin = io.StringIO("123")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_number() == Number(123)


def test_parse_identifier():
    sys.stdin = io.StringIO("habsdajd")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_identifier() == Identifier("habsdajd")


def test_parse_elements():
    sys.stdin = io.StringIO("321, 432, 543)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_elements(Type.CL_BRACKET) == [Number(321), Number(432), Number(543)]


def test_parse_expression_with_plus_and_minus():
    sys.stdin = io.StringIO("2 - 3 + 9")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_expression() == Expression(Expression(Number(2), "-", Number(3)), "+", Number(9))


def test_parse_expression_with_star_and_divide():
    sys.stdin = io.StringIO("5 * 4 / 6")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_expression() == Expression(Expression(Number(5), "*", Number(4)), "/", Number(6))


def test_parse_expression_with_brackets():
    sys.stdin = io.StringIO("9 / (2 + 3)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_expression() == Expression(Number(9), "/", Expression(Number(2), "+", Number(3)))


def test_parse_expression_with_complex_example():
    sys.stdin = io.StringIO("(1 - 9 * 2) / 8 - 6")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    expr = Expression(Expression(Expression(Number(1), "-", Expression(Number(9), "*", Number(2))), "/", Number(8)), "-", Number(6))
    assert parser.parse_expression() == expr


def test_parse_factor_with_identifier():
    sys.stdin = io.StringIO("ksndf")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_factor() == Identifier("ksndf")


def test_parse_factor_with_number():
    sys.stdin = io.StringIO("4375")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_factor() == Number(4375)


def test_parse_factor_with_list():
    sys.stdin = io.StringIO("[8123, [123, 432], fse]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_factor() == List([Number(8123), List([Number(123), Number(432)]), Identifier("fse")])


def test_parse_factor_with_expression():
    sys.stdin = io.StringIO("1 + 2")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_factor() == Number(1)


def test_parse_factor_with_expression_within_brackets():
    sys.stdin = io.StringIO("(1 + 2)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_factor() == Expression(Number(1), "+", Number(2))


def test_parse_function_with_empty_body_and_without_arguments():
    sys.stdin = io.StringIO("function fun(){}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    function = Function(Identifier("fun"), [], None)
    assert parser.parse_function() == function


def test_parse_function_with_empty_body():
    sys.stdin = io.StringIO("function fun(bool arg1, number arg2, list arg3){}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    arg_1 = Variable("bool", Identifier("arg1"), None)
    arg_2 = Variable("number", Identifier("arg2"), None)
    arg_3 = Variable("list", Identifier("arg3"), None)
    function = Function(Identifier("fun"), [arg_1, arg_2, arg_3], None)
    assert parser.parse_function() == function


def test_parse_function_without_arguments():
    sys.stdin = io.StringIO(
        "function fun(){"
        "    a = 1 + (2 * 3);"
        "    return a;"
        "}"
    )
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    line_1 = Expression(Identifier("a"), "=", Expression(Number(1), "+", Expression(Number(2), "*", Number(3))))
    function = Function(Identifier("fun"), [], FunctionBody(Identifier("a"), [line_1]))
    assert parser.parse_function() == function


def test_parse_function_with_arguments_and_body():
    sys.stdin = io.StringIO(
        "function fun(number arg1, number arg2) {"
        "    a = 99 * (2 - 3);"
        "    number x = [g, h, i].get(1);"
        "    print jkl;"
        "    return a;"
        "}"
    )
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    arg_1 = Variable("number", Identifier("arg1"), None)
    arg_2 = Variable("number", Identifier("arg2"), None)
    line_1 = Expression(Identifier("a"), "=", Expression(Number(99), "*", Expression(Number(2), "-", Number(3))))
    line_2 = Variable("number", Identifier("x"), Get(List([Identifier("g"), Identifier("h"), Identifier("i")]), Number(1)))
    line_3 = PrintFunction(Identifier("jkl"))
    function = Function(Identifier("fun"), [arg_1, arg_2], FunctionBody(Identifier("a"), [line_1, line_2, line_3]))
    assert parser.parse_function() == function


def test_parse_function_body_with_empty_return_and_content():
    sys.stdin = io.StringIO("}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    # assert parser.parse_function_body() == FunctionBody(None, None)
    assert parser.parse_function_body() == None


def test_parse_function_body_with_empty_content():
    sys.stdin = io.StringIO("return abc;")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_function_body() == FunctionBody(Identifier("abc"), [])


def test_parse_function_body_with_empty_return():
    sys.stdin = io.StringIO("a = 123 / hi; xyz.delete(3);}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    line_1 = Expression(Identifier("a"), "=", Expression(Number(123), "/", Identifier("hi")))
    line_2 = Delete(Identifier("xyz"), Number(3))
    assert parser.parse_function_body() == FunctionBody(None, [line_1, line_2])


def test_parse_function_body_with_nonempty_return_and_content():
    sys.stdin = io.StringIO("a = 230 / hi; [9, 8, 7].get(3); return 0;}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    line_1 = Expression(Identifier("a"), "=", Expression(Number(230), "/", Identifier("hi")))
    line_2 = Get(List([Number(9), Number(8), Number(7)]), Number(3))
    assert parser.parse_function_body() == FunctionBody(Number(0), [line_1, line_2])


def test_parse_function_body_with_no_semicolon_after_return():
    sys.stdin = io.StringIO("return 0}")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    with pytest.raises(InvalidSyntax):
        assert parser.parse_function_body()


def test_parse_function_call():
    sys.stdin = io.StringIO("(83475, shadowrun, [1231, sdf, [1]])")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    arg_1 = Number(83475)
    arg_2 = Identifier("shadowrun")
    arg_3 = List([Number(1231), Identifier("sdf"), List([Number(1)])])
    function_call = FunctionCall("fun", [arg_1, arg_2, arg_3])
    assert parser.parse_function_call("fun") == function_call


def test_parse_identifier_with_word_and_numbers():
    sys.stdin = io.StringIO("habsdSDFjd9345")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_identifier() == Identifier("habsdSDFjd9345")


def test_parse_identifier_with_number():
    sys.stdin = io.StringIO("123")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    with pytest.raises(InvalidSyntax):
        parser.parse_identifier()


def test_parse_line_with_declaration():
    sys.stdin = io.StringIO("bool abc = [1, 2, 3];")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    variable = Variable("bool", Identifier("abc"), List([Number(1), Number(2), Number(3)]))

    assert parser.parse_line() == variable


def test_parse_line_with_expression():
    sys.stdin = io.StringIO("xyz = [654, 9900, 3123] * 823;")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    identifier = Identifier("xyz")
    tmp_list = List([Number(654), Number(9900), Number(3123)])
    expression = Expression(tmp_list, "*", Number(823))
    result = Expression(Identifier("xyz"), "=", expression)

    assert parser.parse_line() == result


def test_parse_line_with_print():
    sys.stdin = io.StringIO("print abc;")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_line() == PrintFunction(Identifier("abc"))


def test_parse_list_of_numbers():
    sys.stdin = io.StringIO("[69, 70, 71]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_list() == List([Number(69), Number(70), Number(71)])


def test_parse_list_of_identifiers():
    sys.stdin = io.StringIO("[abc, def, ghi]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    assert parser.parse_list() == List([Identifier("abc"), Identifier("def"), Identifier("ghi")])


def test_parse_list_of_lists():
    sys.stdin = io.StringIO("[[1, 2, 3], [[4]], [a, b]]")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    list_1 = List([Number(1), Number(2), Number(3)])
    list_2 = List([List(Number(4))])
    list_3 = List([Identifier("a"), Identifier("b")])
    assert parser.parse_list() == List([list_1, list_2, list_3])


def test_parse_list_component():
    sys.stdin = io.StringIO(".filter(x > xyz).each(-, abc).delete(12).get(3).length()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    condition = FilterCondition(">", Identifier("xyz"))
    conditions = [condition]
    result_1 = Filter(tmp_list, conditions)
    result_2 = Each(result_1, "-", Identifier("abc"))
    result_3 = Delete(result_2, Number(12))
    result_4 = Get(result_3, Number(3))
    result_5 = Length(result_4)

    assert parser.parse_list_component(tmp_list) == result_5


def test_parse_list_component_with_other_word():
    sys.stdin = io.StringIO(".filter(x > 123).xxx(-, abc)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    with pytest.raises(InvalidSyntax):
        parser.parse_list_component(tmp_list)


def test_parse_list_operation_with_delete():
    sys.stdin = io.StringIO(".delete(123)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation(tmp_list) == Delete(tmp_list, Number(123))


def test_parse_list_operation_with_each():
    sys.stdin = io.StringIO(".each(+, 123)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation(tmp_list) == Each(tmp_list, "+", Number(123))


def test_parse_list_operation_with_filter():
    sys.stdin = io.StringIO(".filter(x >= 123 & x == abc)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    conditions = []
    conditions.append(FilterCondition(">=", Number(123)))
    conditions.append(FilterCondition("==", Identifier("abc")))
    assert parser.parse_list_operation(tmp_list) == Filter(tmp_list, conditions)


def test_parse_list_operation_with_get():
    sys.stdin = io.StringIO(".get(xyz)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    assert parser.parse_list_operation(tmp_list) == Get(tmp_list, Identifier("xyz"))


def test_parse_list_operation_with_length():
    sys.stdin = io.StringIO(".length()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    assert parser.parse_list_operation(tmp_list) == Length(tmp_list)


def test_parse_list_operation_with_other_word():
    sys.stdin = io.StringIO(".sadfafasa()")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    with pytest.raises(InvalidSyntax):
        parser.parse_list_operation(tmp_list)


def test_parse_list_operation_delete_with_number():
    sys.stdin = io.StringIO("delete(123)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_delete(tmp_list) == Delete(tmp_list, Number(123))


def test_parse_list_operation_delete_with_identifier():
    sys.stdin = io.StringIO("delete(abc)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_delete(tmp_list) == Delete(tmp_list, Identifier("abc"))   


def test_parse_list_operation_each():
    sys.stdin = io.StringIO("each(+, 1)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_each(tmp_list) == Each(tmp_list, "+", Number(1))


def test_parse_list_operation_each_with_complex_expression():
    sys.stdin = io.StringIO("each(+, 1 + 2 * abc)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    expression = Expression(Number(1), "+", Expression(Number(2), "*", Identifier("abc")))
    assert parser.parse_list_operation_each(tmp_list) == Each(tmp_list, "+", expression)


def test_parse_list_operation_filter():
    sys.stdin = io.StringIO("filter(x > 1 & x < 999 & x >= abc & x <= xyz)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    conditions = []
    conditions.append(FilterCondition(">", Number(1)))
    conditions.append(FilterCondition("<", Number(999)))
    conditions.append(FilterCondition(">=", Identifier("abc")))
    conditions.append(FilterCondition("<=", Identifier("xyz")))
    assert parser.parse_list_operation_filter(tmp_list) == Filter(tmp_list, conditions)


def test_parse_list_operation_filter_with_different_list():
    sys.stdin = io.StringIO("filter(x > 1 & x < 999 & x >= abc & x <= xyz)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]

    conditions = []
    conditions.append(FilterCondition(">", Number(1)))
    conditions.append(FilterCondition("<", Number(999)))
    conditions.append(FilterCondition(">=", Identifier("abc")))
    conditions.append(FilterCondition("<=", Identifier("xyz")))
    assert parser.parse_list_operation_filter(list_1) != Filter(list_2, conditions)


def test_parse_list_operation_filter_with_different_conditions():
    sys.stdin = io.StringIO("filter(x > 1 & x < 999 & x >= abc & x <= xyz)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]

    conditions = []
    conditions.append(FilterCondition("==", Number(1)))
    conditions.append(FilterCondition(">", Number(999)))
    conditions.append(FilterCondition("<", Identifier("abc")))
    conditions.append(FilterCondition("<=", Identifier("xyz")))
    assert parser.parse_list_operation_filter(tmp_list) != Filter(tmp_list, conditions)


def test_parse_list_operation_get_with_number():
    sys.stdin = io.StringIO("get(1)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_get(tmp_list) == Get(tmp_list, Number(1))


def test_parse_list_operation_get_with_identifier():
    sys.stdin = io.StringIO("get(abc)")
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)

    tmp_list = [1, 2, 3]
    assert parser.parse_list_operation_get(tmp_list) == Get(tmp_list, Identifier("abc"))


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

    assert parser.parse_list_operation_length(list_1) != Length(list_2)


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
