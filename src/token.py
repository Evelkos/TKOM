# token.py
from enum import Enum, auto

class Type(Enum):
    EOF = auto()
    IDENTIFIER = auto()
    LIST_TYPE = auto()
    NUMBER = auto()
    NUMBER_TYPE = auto()
    BOOL = auto()
    BOOL_TYPE = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    DIVIDE = auto()
    OP_SQUARE_BRACKET = auto()
    CL_SQUARE_BRACKET = auto()
    OP_BRACKET = auto()
    CL_BRACKET = auto()
    OP_CURLY_BRACKET = auto()
    CL_CURLY_BRACKET = auto()
    SEMICOLON = auto()
    DOT = auto()
    COMMA = auto()
    NOT = auto()
    RETURN = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    LESS_OR_EQUAL_TO = auto()
    GREATER_OR_EQUAL_TO = auto()
    ASSIGN = auto()
    EQUAL_TO = auto()
    NOT_EQUAL_TO = auto()
    AND = auto()
    OR = auto()
    FILTER = auto()
    EACH = auto()
    GET = auto()
    LENGTH = auto()
    DELETE = auto()
    UNIDENTIFIED = auto()
    # MAIN = auto()
    FUNCTION = auto()
    PRINT = auto()

class Symbol:
    special_characters = {
        '[': Type.OP_SQUARE_BRACKET,
        ']': Type.CL_SQUARE_BRACKET,
        '(': Type.OP_BRACKET,
        ')': Type.CL_BRACKET,
        '{': Type.OP_CURLY_BRACKET,
        '}': Type.CL_CURLY_BRACKET,
        '*': Type.STAR,
        '/': Type.DIVIDE,
        '+': Type.PLUS,
        '-': Type.MINUS,
        ';': Type.SEMICOLON,
        '.': Type.DOT,
        ',': Type.COMMA,
        '!': Type.NOT,
        '<': Type.LESS_THAN,
        '>': Type.GREATER_THAN,
        '=': Type.ASSIGN,
        '&': Type.AND,
        '|': Type.OR
    }

    double_operators = {
        '<=': Type.LESS_OR_EQUAL_TO,
        '>=': Type.GREATER_OR_EQUAL_TO,
        '==': Type.EQUAL_TO,
        '!=': Type.NOT_EQUAL_TO
    }

    key_words = {
        'list': Type.LIST_TYPE,
        'number': Type.NUMBER_TYPE,
        'bool': Type.BOOL_TYPE,
        'true': Type.BOOL,
        'false': Type.BOOL,
        'return': Type.RETURN,
        'filter': Type.FILTER,
        'each': Type.EACH,
        'get': Type.GET,
        'length': Type.LENGTH,
        'delete': Type.DELETE,
        # 'main': Type.MAIN,
        'function' : Type.FUNCTION,
        'print': Type.PRINT,
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
