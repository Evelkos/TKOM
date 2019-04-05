# token.py
from enum import Enum, auto

class Type(Enum):
    EOF = auto()
    IDENTIFIER = auto()
    LIST = auto()
    NUMBER = auto()
    BOOL = auto()
    ADD_OPERATOR = auto()
    MULT_OPERATOR = auto()
    OP_SQUARE_BRACKET = auto()
    CL_SQUARE_BRACKET = auto()
    OP_BRACKET = auto()
    CL_BRACKET = auto()
    OP_CURLY_BRACKET = auto()
    CL_CURLY_BRACKET = auto()
    SEMICOLON = auto()
    DOT = auto()
    COMMA = auto()
    RETURN = auto()

class Symbol:
    special_characters = {
        '[': Type.OP_SQUARE_BRACKET,
        ']': Type.CL_SQUARE_BRACKET,
        '(': Type.OP_BRACKET,
        ')': Type.CL_BRACKET,
        '{': Type.OP_CURLY_BRACKET,
        '}': Type.CL_CURLY_BRACKET,
        '*': Type.MULT_OPERATOR,
        '/': Type.MULT_OPERATOR,
        '+': Type.ADD_OPERATOR,
        '-': Type.ADD_OPERATOR,
        ';': Type.SEMICOLON,
        '.': Type.DOT,
        ',': Type.COMMA
    }

    key_words = {
        'list': Type.LIST,
        'number': Type.NUMBER,
        'bool': Type.BOOL,
        'return': Type.RETURN
    }


class Token:
    def __init__(self, token_type = Type.IDENTIFIER, value = ""):
        self.token_type = token_type
        self.value = value


    def __repr__(self):
        return f"(token_type={self.token_type}, value={self.value})"


    def get_type(self):
        return self.token_type


    def get_value(self):
        return self.value
