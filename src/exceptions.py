# exceptions.py

class InvalidSyntax(Exception):
    """Invalid syntax error"""
    def __init__(self, position = (0, 0), expected_type = None, given_type = None, given_value = None):
    	self.position = position
    	self.expected_type = expected_type
    	self.given_type = given_type
    	self.given_value = given_value