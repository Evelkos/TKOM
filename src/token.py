# token.py
from enum import Enum, auto

class Type(Enum):
    EOF = auto()
    IDENTIFIER = auto()
    LIST = auto()
    NUMBER = auto()
    BOOL = auto()


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
