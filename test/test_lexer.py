import sys, os
import pytest
from TKOM.src.token import Type, Token
from TKOM.src.lexer import Lexer


def test_lexer_with_single_identifier(tmpdir):
    tmp = tmpdir.mkdir("tmp")
    file = tmp.join("file.txt")
    file.write("identifier")

    token = Token(Type.IDENTIFIER, "identifier")
    lexer = Lexer(str(tmp / "file.txt"))
    lexer.build_next_token()

    assert lexer.get_token().get_value() == token.get_value()
    assert lexer.get_token().get_type() == token.get_type()
    assert str(lexer.get_token()) == str(token)

def test_a():
    assert Type.EOF.value == 1
    assert Type.IDENTIFIER.value == 2
