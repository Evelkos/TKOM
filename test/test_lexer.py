import sys
import pytest
from TKOM.src.token import Type, Token
from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
import io

def create_lexer(string):
    return Lexer(Source(io.StringIO(string)))

def test_lexer_with_single_identifier():
    lexer = create_lexer("identifier")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier"
    assert lexer.get_token().get_type() == Type.IDENTIFIER


def test_lexer_with_multiple_identifiers():
    lexer = create_lexer("identifier1 identifier2")

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
    lexer = create_lexer("123")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_multiple_numbers():
    lexer = create_lexer("123 456")

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
    lexer = create_lexer("list")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "list"
    assert lexer.get_token().get_type() == Type.LIST_TYPE


def test_lexer_with_key_word_number():
    lexer = create_lexer("number")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "number"
    assert lexer.get_token().get_type() == Type.NUMBER_TYPE


def test_lexer_with_key_word_bool():
    lexer = create_lexer("bool")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "bool"
    assert lexer.get_token().get_type() == Type.BOOL_TYPE


def test_lexer_with_key_word_return():
    lexer = create_lexer("return")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "return"
    assert lexer.get_token().get_type() == Type.RETURN


def test_lexer_with_key_word_filter():
    lexer = create_lexer("filter")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "filter"
    assert lexer.get_token().get_type() == Type.FILTER


def test_lexer_with_key_word_each():
    lexer = create_lexer("each")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "each"
    assert lexer.get_token().get_type() == Type.EACH


def test_lexer_with_key_word_get():
    lexer = create_lexer("get")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "get"
    assert lexer.get_token().get_type() == Type.GET


def test_lexer_with_key_word_length():
    lexer = create_lexer("length")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "length"
    assert lexer.get_token().get_type() == Type.LENGTH


def test_lexer_with_key_word_delete():
    lexer = create_lexer("delete")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "delete"
    assert lexer.get_token().get_type() == Type.DELETE


def test_lexer_with_key_word_true():
    lexer = create_lexer("true")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "true"
    assert lexer.get_token().get_type() == Type.BOOL


def test_lexer_with_key_word_false():
    lexer = create_lexer("false")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "false"
    assert lexer.get_token().get_type() == Type.BOOL


def test_lexer_with_key_word_eof():
    lexer = create_lexer("")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_key_word_function():
    lexer = create_lexer("function")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "function"
    assert lexer.get_token().get_type() == Type.FUNCTION


def test_lexer_with_key_word_print():
    lexer = create_lexer("print")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "print"
    assert lexer.get_token().get_type() == Type.PRINT


def test_lexer_with_special_character_OP_SQUARE_BRACKET():
    lexer = create_lexer("[")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "["
    assert lexer.get_token().get_type() == Type.OP_SQUARE_BRACKET


def test_lexer_with_special_character_CL_SQUARE_BRACKET():
    lexer = create_lexer("]")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "]"
    assert lexer.get_token().get_type() == Type.CL_SQUARE_BRACKET


def test_lexer_with_special_character_OP_BRACKET():
    lexer = create_lexer("(")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "("
    assert lexer.get_token().get_type() == Type.OP_BRACKET


def test_lexer_with_special_character_CL_BRACKET():
    lexer = create_lexer(")")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ")"
    assert lexer.get_token().get_type() == Type.CL_BRACKET


def test_lexer_with_special_character_OP_CURLY_BRACKET():
    lexer = create_lexer("{")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "{"
    assert lexer.get_token().get_type() == Type.OP_CURLY_BRACKET


def test_lexer_with_special_character_CL_CURLY_BRACKET():
    lexer = create_lexer("}")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "}"
    assert lexer.get_token().get_type() == Type.CL_CURLY_BRACKET


def test_lexer_with_special_character_STAR():
    lexer = create_lexer("*")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "*"
    assert lexer.get_token().get_type() == Type.STAR


def test_lexer_with_special_character_DIVIDE():
    lexer = create_lexer("/")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "/"
    assert lexer.get_token().get_type() == Type.DIVIDE


def test_lexer_with_special_character_DIVIDE():
    lexer = create_lexer("+")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "+"
    assert lexer.get_token().get_type() == Type.PLUS


def test_lexer_with_special_character_MINUS():
    lexer = create_lexer("-")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "-"
    assert lexer.get_token().get_type() == Type.MINUS


def test_lexer_with_special_character_SEMICOLON():
    lexer = create_lexer(";")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ";"
    assert lexer.get_token().get_type() == Type.SEMICOLON


def test_lexer_with_special_character_DOT():
    lexer = create_lexer(".")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "."
    assert lexer.get_token().get_type() == Type.DOT


def test_lexer_with_special_character_COMMA():
    lexer = create_lexer(",")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ","
    assert lexer.get_token().get_type() == Type.COMMA


def test_lexer_with_special_character_NOT():
    lexer = create_lexer("!")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!"
    assert lexer.get_token().get_type() == Type.NOT


def test_lexer_with_special_character_LESS_THAN():
    lexer = create_lexer("<")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<"
    assert lexer.get_token().get_type() == Type.LESS_THAN


def test_lexer_with_special_character_GREATER_THAN():
    lexer = create_lexer(">")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">"
    assert lexer.get_token().get_type() == Type.GREATER_THAN


def test_lexer_with_special_character_ASSIGN():
    lexer = create_lexer("=")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "="
    assert lexer.get_token().get_type() == Type.ASSIGN


def test_lexer_with_special_character_AND():
    lexer = create_lexer("&")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "&"
    assert lexer.get_token().get_type() == Type.AND


def test_lexer_with_special_character_OR():
    lexer = create_lexer("|")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "|"
    assert lexer.get_token().get_type() == Type.OR


def test_lexer_with_special_character_EOF():
    lexer = create_lexer("")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_double_operator_LESS_OR_EQUAL_TO():
    lexer = create_lexer("<=")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<="
    assert lexer.get_token().get_type() == Type.LESS_OR_EQUAL_TO


def test_lexer_with_double_operator_GREATER_OR_EQUAL_TO():
    lexer = create_lexer(">=")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">="
    assert lexer.get_token().get_type() == Type.GREATER_OR_EQUAL_TO


def test_lexer_with_double_operator_EQUAL_TO():
    lexer = create_lexer("==")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "=="
    assert lexer.get_token().get_type() == Type.EQUAL_TO


def test_lexer_with_double_operator_NOT_EQUAL_TO():
    lexer = create_lexer("!=")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!="
    assert lexer.get_token().get_type() == Type.NOT_EQUAL_TO


def test_lexer_with_single_comment():
    lexer = create_lexer("abc # ghi\njkl")

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
    lexer = create_lexer("abc #")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_just_a_comment():
    lexer = create_lexer("#")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_complex_input():
    lexer = create_lexer("abc =123| list& }  abc!")

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
