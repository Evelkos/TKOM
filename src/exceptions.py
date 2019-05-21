# exceptions.py


class DivisionError(Exception):
    def __init__(self):
        super().__init__()

class InvalidSyntax(Exception):
    def __init__(self, position=(0, 0), expected_type=None, given_type=None, given_value=None):
        self.position = position
        self.expected_type = expected_type
        self.given_type = given_type
        self.given_value = given_value


class InvalidValue(Exception):
    def __init__(self, expected_type, given_type):
        self.expected_type = expected_type
        self.given_type = given_type


class UndefinedOperation(Exception):
    def __init__(self, left_operand, operation, right_operand):
        self.left_operand = left_operand
        self.operation = operation
        self.right_operand = right_operand


class InvalidOperation(Exception):
    def __init__(self, left_operand, operation, right_operand):
        self.left_operand = left_operand
        self.operation = operation
        self.right_operand = right_operand


class Undeclared(Exception):
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name


class IndexOutOfRange(Exception):
    def __init__(self):
        super().__init__()