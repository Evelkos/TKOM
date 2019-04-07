import sys, os
import pytest
from TKOM.src.token import Type, Token
from TKOM.src.lexer import Lexer


def test_lexer_with_single_identifier(tmp_path):
    file = tmp_path / "test_lexer_with_single_identifier.txt"
    file.write_text("identifier identifier2")

    lexer = Lexer(tmp_path / "test_lexer_with_single_identifier.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier"
    assert lexer.get_token().get_type() == Type.IDENTIFIER


def test_lexer_with_multiple_identifiers(tmp_path):
    file = tmp_path / "test_lexer_with_multiple_identifiers.txt"
    file.write_text("identifier1 identifier2")

    lexer = Lexer(tmp_path / "test_lexer_with_multiple_identifiers.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier1"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "identifier2"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_single_number(tmp_path):
    file = tmp_path / "test_lexer_with_single_number.txt"
    file.write_text("123")

    lexer = Lexer(tmp_path / "test_lexer_with_single_number.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_multiple_numbers(tmp_path):
    file = tmp_path / "test_lexer_with_multiple_numbers.txt"
    file.write_text("123 456")

    lexer = Lexer(tmp_path / "test_lexer_with_multiple_numbers.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "123"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "456"
    assert lexer.get_token().get_type() == Type.NUMBER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_key_words(tmp_path):
    file = tmp_path / "test_lexer_with_key_words.txt"
    file.write_text("list number bool return filter each get length delete")

    lexer = Lexer(tmp_path / "test_lexer_with_key_words.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "list"
    assert lexer.get_token().get_type() == Type.LIST_TYPE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "number"
    assert lexer.get_token().get_type() == Type.NUMBER_TYPE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "bool"
    assert lexer.get_token().get_type() == Type.BOOL_TYPE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "return"
    assert lexer.get_token().get_type() == Type.RETURN
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "filter"
    assert lexer.get_token().get_type() == Type.FILTER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "each"
    assert lexer.get_token().get_type() == Type.EACH
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "get"
    assert lexer.get_token().get_type() == Type.GET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "length"
    assert lexer.get_token().get_type() == Type.LENGTH
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "delete"
    assert lexer.get_token().get_type() == Type.DELETE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_special_characters(tmp_path):
    file = tmp_path / "test_lexer_with_special_characters.txt"
    file.write_text("[ ] ( ) { } * / + - ; . , ! < > = & |")

    lexer = Lexer(tmp_path / "test_lexer_with_special_characters.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "["
    assert lexer.get_token().get_type() == Type.OP_SQUARE_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "]"
    assert lexer.get_token().get_type() == Type.CL_SQUARE_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "("
    assert lexer.get_token().get_type() == Type.OP_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == ")"
    assert lexer.get_token().get_type() == Type.CL_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "{"
    assert lexer.get_token().get_type() == Type.OP_CURLY_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "}"
    assert lexer.get_token().get_type() == Type.CL_CURLY_BRACKET
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "*"
    assert lexer.get_token().get_type() == Type.STAR
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "/"
    assert lexer.get_token().get_type() == Type.DIVIDE
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "+"
    assert lexer.get_token().get_type() == Type.PLUS
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "-"
    assert lexer.get_token().get_type() == Type.MINUS
    lexer.build_next_token()
    assert lexer.get_token().get_value() == ";"
    assert lexer.get_token().get_type() == Type.SEMICOLON
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "."
    assert lexer.get_token().get_type() == Type.DOT
    lexer.build_next_token()
    assert lexer.get_token().get_value() == ","
    assert lexer.get_token().get_type() == Type.COMMA
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!"
    assert lexer.get_token().get_type() == Type.NOT
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<"
    assert lexer.get_token().get_type() == Type.LESS_THAN
    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">"
    assert lexer.get_token().get_type() == Type.GREATER_THAN
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "="
    assert lexer.get_token().get_type() == Type.ASSIGN
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "&"
    assert lexer.get_token().get_type() == Type.AND
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "|"
    assert lexer.get_token().get_type() == Type.OR
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_double_operators(tmp_path):
    file = tmp_path / "test_lexer_with_double_operators.txt"
    file.write_text("<= >= == !=")

    lexer = Lexer(tmp_path / "test_lexer_with_double_operators.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "<="
    assert lexer.get_token().get_type() == Type.LESS_OR_EQUAL_TO
    lexer.build_next_token()
    assert lexer.get_token().get_value() == ">="
    assert lexer.get_token().get_type() == Type.GREATER_OR_EQUAL_TO
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "=="
    assert lexer.get_token().get_type() == Type.EQUAL_TO
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "!="
    assert lexer.get_token().get_type() == Type.NOT_EQUAL_TO
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF

def test_lexer_with_single_comment(tmp_path):
    file = tmp_path / "test_lexer_with_single_comment.txt"
    file.write_text("abc # ghi\njkl")

    lexer = Lexer(tmp_path / "test_lexer_with_single_comment.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == "jkl"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF

def test_lexer_with_the_comment_at_the_end_of_the_file(tmp_path):
    file = tmp_path / "test_comment_at_the_end_of_the_file.txt"
    file.write_text("abc #")

    lexer = Lexer(tmp_path / "test_comment_at_the_end_of_the_file.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == "abc"
    assert lexer.get_token().get_type() == Type.IDENTIFIER
    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_just_a_comment(tmp_path):
    file = tmp_path / "test_lexer_with_just_a_comment.txt"
    file.write_text("#")

    lexer = Lexer(tmp_path / "test_lexer_with_just_a_comment.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_empty_file(tmp_path):
    file = tmp_path / "test_lexer_with_empty_file.txt"
    file.write_text("")

    lexer = Lexer(tmp_path / "test_lexer_with_empty_file.txt")

    lexer.build_next_token()
    assert lexer.get_token().get_value() == None
    assert lexer.get_token().get_type() == Type.EOF


def test_lexer_with_complex_file(tmp_path):
    file = tmp_path / "test_lexer_with_complex_file.txt"
    file.write_text("abc =123| list& }  abc!")

    lexer = Lexer(tmp_path / "test_lexer_with_complex_file.txt")

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
