import sys
import pytest
from TKOM.src.token import Type, Token
from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
import io


def test_lexer_with_single_identifier():
    sys.stdin = io.StringIO("identifier")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier"
    assert lexer.get_token().get_type() == Type.IDENTIFIER


def test_lexer_with_multiple_identifiers():
    sys.stdin = io.StringIO("identifier1 identifier2")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier1"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier2"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_single_number():
    sys.stdin = io.StringIO("123")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_multiple_numbers():
    sys.stdin = io.StringIO("123 456")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "456"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_key_word_list():
    sys.stdin = io.StringIO("list")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "list"
    assert lexer.get_token().get_type() == Type.LIST_TYPE


def test_lexer_with_key_word_number():
    sys.stdin = io.StringIO("number")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "number"
    assert lexer.get_token().get_type() == Type.NUMBER_TYPE


def test_lexer_with_key_word_bool():
    sys.stdin = io.StringIO("bool")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "bool"
    assert lexer.get_token().get_type() == Type.BOOL_TYPE


def test_lexer_with_key_word_return():
    sys.stdin = io.StringIO("return")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "return"
    assert lexer.get_token().get_type() == Type.RETURN


def test_lexer_with_key_word_filter():
    sys.stdin = io.StringIO("filter")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "filter"
    assert lexer.get_token().get_type() == Type.FILTER


def test_lexer_with_key_word_each():
    sys.stdin = io.StringIO("each")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "each"
    assert lexer.get_token().get_type() == Type.EACH


def test_lexer_with_key_word_get():
    sys.stdin = io.StringIO("get")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "get"
    assert lexer.get_token().get_type() == Type.GET


def test_lexer_with_key_word_length():
    sys.stdin = io.StringIO("length")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "length"
    assert lexer.get_token().get_type() == Type.LENGTH


def test_lexer_with_key_word_delete():
    sys.stdin = io.StringIO("delete")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "delete"
    assert lexer.get_token().get_type() == Type.DELETE


def test_lexer_with_key_word_true():
    sys.stdin = io.StringIO("true")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "true"
    assert lexer.get_token().get_type() == Type.BOOL


def test_lexer_with_key_word_false():
    sys.stdin = io.StringIO("false")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "false"
    assert lexer.get_token().get_type() == Type.BOOL


def test_lexer_with_key_word_eof():
    sys.stdin = io.StringIO("")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_key_word_main():
    sys.stdin = io.StringIO("main")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "main"
    assert lexer.get_token().get_type() == Type.MAIN


def test_lexer_with_key_word_function():
    sys.stdin = io.StringIO("function")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "function"
    assert lexer.get_token().get_type() == Type.FUNCTION


def test_lexer_with_key_word_print():
    sys.stdin = io.StringIO("print")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "print"
    assert lexer.get_token().get_type() == Type.PRINT


def test_lexer_with_special_character_OP_SQUARE_BRACKET():
    sys.stdin = io.StringIO("[")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "["
    assert lexer.get_token().get_type() == Type.OP_SQUARE_BRACKET


def test_lexer_with_special_character_CL_SQUARE_BRACKET():
    sys.stdin = io.StringIO("]")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "]"
    assert lexer.get_token().get_type() == Type.CL_SQUARE_BRACKET


def test_lexer_with_special_character_OP_BRACKET():
    sys.stdin = io.StringIO("(")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "("
    assert lexer.get_token().get_type() == Type.OP_BRACKET


def test_lexer_with_special_character_CL_BRACKET():
    sys.stdin = io.StringIO(")")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ")"
    assert lexer.get_token().get_type() == Type.CL_BRACKET


def test_lexer_with_special_character_OP_CURLY_BRACKET():
    sys.stdin = io.StringIO("{")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "{"
    assert lexer.get_token().get_type() == Type.OP_CURLY_BRACKET


def test_lexer_with_special_character_CL_CURLY_BRACKET():
    sys.stdin = io.StringIO("}")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "}"
    assert lexer.get_token().get_type() == Type.CL_CURLY_BRACKET


def test_lexer_with_special_character_STAR():
    sys.stdin = io.StringIO("*")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "*"
    assert lexer.get_token().get_type() == Type.STAR


def test_lexer_with_special_character_DIVIDE():
    sys.stdin = io.StringIO("/")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "/"
    assert lexer.get_token().get_type() == Type.DIVIDE


def test_lexer_with_special_character_DIVIDE():
    sys.stdin = io.StringIO("+")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "+"
    assert lexer.get_token().get_type() == Type.PLUS


def test_lexer_with_special_character_MINUS():
    sys.stdin = io.StringIO("-")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "-"
    assert lexer.get_token().get_type() == Type.MINUS


def test_lexer_with_special_character_SEMICOLON():
    sys.stdin = io.StringIO(";")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ";"
    assert lexer.get_token().get_type() == Type.SEMICOLON


def test_lexer_with_special_character_DOT():
    sys.stdin = io.StringIO(".")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "."
    assert lexer.get_token().get_type() == Type.DOT


def test_lexer_with_special_character_COMMA():
    sys.stdin = io.StringIO(",")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ","
    assert lexer.get_token().get_type() == Type.COMMA


def test_lexer_with_special_character_NOT():
    sys.stdin = io.StringIO("!")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!"
    assert lexer.get_token().get_type() == Type.NOT


def test_lexer_with_special_character_LESS_THAN():
    sys.stdin = io.StringIO("<")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<"
    assert lexer.get_token().get_type() == Type.LESS_THAN


def test_lexer_with_special_character_GREATER_THAN():
    sys.stdin = io.StringIO(">")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">"
    assert lexer.get_token().get_type() == Type.GREATER_THAN


def test_lexer_with_special_character_ASSIGN():
    sys.stdin = io.StringIO("=")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "="
    assert lexer.get_token().get_type() == Type.ASSIGN


def test_lexer_with_special_character_AND():
    sys.stdin = io.StringIO("&")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "&"
    assert lexer.get_token().get_type() == Type.AND


def test_lexer_with_special_character_OR():
    sys.stdin = io.StringIO("|")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "|"
    assert lexer.get_token().get_type() == Type.OR


def test_lexer_with_special_character_EOF():
    sys.stdin = io.StringIO("")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_double_operator_LESS_OR_EQUAL_TO():
    sys.stdin = io.StringIO("<=")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<="
    assert lexer.get_token().get_type() == Type.LESS_OR_EQUAL_TO


def test_lexer_with_double_operator_GREATER_OR_EQUAL_TO():
    sys.stdin = io.StringIO(">=")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">="
    assert lexer.get_token().get_type() == Type.GREATER_OR_EQUAL_TO


def test_lexer_with_double_operator_EQUAL_TO():
    sys.stdin = io.StringIO("==")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "=="
    assert lexer.get_token().get_type() == Type.EQUAL_TO


def test_lexer_with_double_operator_NOT_EQUAL_TO():
    sys.stdin = io.StringIO("!=")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!="
    assert lexer.get_token().get_type() == Type.NOT_EQUAL_TO


def test_lexer_with_single_comment():
    sys.stdin = io.StringIO("abc # ghi\njkl")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "jkl"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_the_comment_at_the_end_of_the_file():
    sys.stdin = io.StringIO("abc #")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_just_a_comment():
    sys.stdin = io.StringIO("#")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_empty_input():
    sys.stdin = io.StringIO("")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_complex_input():
    sys.stdin = io.StringIO("abc =123| list& }  abc!")
    source = Source()
    lexer = Lexer(source)

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "="
    assert lexer.get_token().get_type() == Type.ASSIGN
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "|"
    assert lexer.get_token().get_type() == Type.OR
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "list"
    assert lexer.get_token().get_type() == Type.LIST_TYPE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "&"
    assert lexer.get_token().get_type() == Type.AND
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "}"
    assert lexer.get_token().get_type() == Type.CL_CURLY_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!"
    assert lexer.get_token().get_type() == Type.NOT
