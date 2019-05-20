from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
from TKOM.src.parser import Parser
from TKOM.src.visitor import Visitor
from TKOM.src.interpreter import Interpreter
import io

def create_interpreter(string):
    source = Source(io.StringIO(string))
    lexer = Lexer(source)
    return Interpreter(Parser(source, lexer), Visitor())


def test_interpreter_run_without_main():
    interpreter = create_interpreter(" \
        function fun1() { } \
        function fun2() { } \
    ")
    assert interpreter.run() == None

def test_interpreter_with_empty_main():
    interpreter = create_interpreter(" \
        function fun1() { } \
        function main() { } \
    ")
    assert interpreter.run() == None