from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
from TKOM.src.parser import Parser
from TKOM.src.visitor import Visitor
from TKOM.src.interpreter import Interpreter
from TKOM.src.exceptions import UndefinedOperation, InvalidOperation, Undeclared, InvalidValue, InvalidSyntax
import io
import pytest

def create_interpreter(string):
    source = Source(io.StringIO(string))
    lexer = Lexer(source)
    return Interpreter(Parser(source, lexer), Visitor())


def test_interpreter_run_without_main():
    interpreter = create_interpreter("function fun1() { } function fun2() { }")
    assert interpreter.run() == None


def test_interpreter_run_with_empty_main():
    interpreter = create_interpreter("function main(){ }")
    assert interpreter.run() == None


def test_interpreter_run_with_number_return_in_main():
    interpreter = create_interpreter("function main(){ return 312; }")
    assert interpreter.run() == 312


def test_interpreter_run_with_false_return_in_main():
    interpreter = create_interpreter("function main(){ return false; }")
    assert interpreter.run() == False


def test_interpreter_run_with_true_return_in_main():
    interpreter = create_interpreter("function main(){ return true; }")
    assert interpreter.run() == True


def test_interpreter_run_with_list_return_in_main():
    interpreter = create_interpreter("function main(){ return [9, 123, 43]; }")
    assert interpreter.run() == [9, 123, 43]


def test_interpreter_run_with_empty_return_in_main():
    interpreter = create_interpreter("function main(){ return; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()


def test_interpreter_run_with_number_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ number a = 81236138; return a; }")
    assert interpreter.run() == 81236138


def test_interpreter_run_with_number_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { number a; a = 2876239; return a; }")
    assert interpreter.run() == 2876239


def test_interpreter_run_with_bool_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ bool a = true; return a; }")
    assert interpreter.run() == True


def test_interpreter_run_with_bool_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { bool a; a = false; return a; }")
    assert interpreter.run() == False


def test_interpreter_run_with_list_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ list a = [6, 2, 999]; return a; }")
    assert interpreter.run() == [6, 2, 999]


def test_interpreter_run_with_list_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { list a; a = [77, 23, 69, 1]; return a; }")
    assert interpreter.run() == [77, 23, 69, 1]


def test_interpreter_run_with_number_variable_reassigned():
    interpreter = create_interpreter("function main() { number a = 1; a = 2; a = 3; return a; }")
    assert interpreter.run() == 3


def test_interpreter_run_with_bool_variable_reassigned_with_false():
    interpreter = create_interpreter("function main() { bool a = true; a = false; return a; }")
    assert interpreter.run() == False


def test_interpreter_run_with_bool_variable_reassigned_with_true():
    interpreter = create_interpreter("function main() { bool a = false; a = true; return a; }")
    assert interpreter.run() == True


def test_interpreter_run_with_list_variable_reassigned():
    interpreter = create_interpreter("function main() { list a = [5, 7, 2]; a = [1]; a = [93, 44]; return a; }")
    assert interpreter.run() == [93, 44]

def test_interpreter_run_with_addition_expression():
    interpreter = create_interpreter("function main() { return 123 + 321; }")
    assert interpreter.run() == 444