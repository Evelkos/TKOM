# token.py
from enum import Enum

class Type(Enum):
    IDENTIFIER = 1
    LIST = 2
    NUMBER = 3
    BOOL = 4


class Token:
    def __init__(self, token_type = Type.IDENTIFIER, value = 0):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"(token_type={self.token_type}, value={self.value})"


    def get_type(self):
        return self.token_type


    def get_value(self):
        return self.value
