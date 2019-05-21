from TKOM.src.lexer import Lexer
from TKOM.src.source import Source
from TKOM.src.parser import Parser
from TKOM.src.visitor import Visitor
from TKOM.src.interpreter import Interpreter
from TKOM.src.exceptions import (
    DivisionError,
    UndefinedOperation,
    InvalidOperation,
    Undeclared,
    InvalidValue,
    InvalidSyntax,
    IndexOutOfRange
)
import io
import pytest

def create_interpreter(string):
    source = Source(io.StringIO(string))
    lexer = Lexer(source)
    return Interpreter(Parser(source, lexer), Visitor())


def test_interpreter_without_main():
    interpreter = create_interpreter("function fun1() { } function fun2() { }")
    assert interpreter.run() == None


def test_interpreter_with_empty_main():
    interpreter = create_interpreter("function main(){ }")
    assert interpreter.run() == None


def test_interpreter_without_return_statement_and_with_nonempty_content_in_main():
    interpreter = create_interpreter("function main(){ 1 + 1; }")
    assert interpreter.run() == None


def test_interpreter_with_empty_content_in_main():
    interpreter = create_interpreter("function main(){ return 312; }")
    assert interpreter.run() == 312


def test_interpreter_with_false_return_in_main():
    interpreter = create_interpreter("function main(){ return false; }")
    assert interpreter.run() == False


def test_interpreter_with_true_return_in_main():
    interpreter = create_interpreter("function main(){ return true; }")
    assert interpreter.run() == True


def test_interpreter_with_list_return_in_main():
    interpreter = create_interpreter("function main(){ return [9, 123, 43]; }")
    assert interpreter.run() == [9, 123, 43]


def test_interpreter_with_empty_return_in_main():
    interpreter = create_interpreter("function main(){ return; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()


def test_interpreter_with_number_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ number a = 81236138; return a; }")
    assert interpreter.run() == 81236138


def test_interpreter_with_number_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { number a; a = 2876239; return a; }")
    assert interpreter.run() == 2876239


def test_interpreter_with_number_type_variable_declaration_and_minus_in_return_statement():
    interpreter = create_interpreter("function main() { number a = 2876239; return -a; }")
    assert interpreter.run() == -2876239


def test_interpreter_with_bool_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ bool a = true; return a; }")
    assert interpreter.run() == True


def test_interpreter_with_bool_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { bool a; a = false; return a; }")
    assert interpreter.run() == False


def test_interpreter_with_list_type_variable_declaration_with_assign():
    interpreter = create_interpreter("function main(){ list a = [6, 2, 999]; return a; }")
    assert interpreter.run() == [6, 2, 999]


def test_interpreter_with_list_type_variable_declaration_and_assign():
    interpreter = create_interpreter("function main() { list a; a = [77, 23, 69, 1]; return a; }")
    assert interpreter.run() == [77, 23, 69, 1]


def test_interpreter_with_number_variable_reassigned():
    interpreter = create_interpreter("function main() { number a = 1; a = 2; a = 3; return a; }")
    assert interpreter.run() == 3


def test_interpreter_with_bool_variable_reassigned_with_false():
    interpreter = create_interpreter("function main() { bool a = true; a = false; return a; }")
    assert interpreter.run() == False


def test_interpreter_with_bool_variable_reassigned_with_true():
    interpreter = create_interpreter("function main() { bool a = false; a = true; return a; }")
    assert interpreter.run() == True


def test_interpreter_with_list_variable_reassigned():
    interpreter = create_interpreter("function main() { list a = [5, 7, 2]; a = [1]; a = [93, 44]; return a; }")
    assert interpreter.run() == [93, 44]


def test_interpreter_with_addition_expression():
    interpreter = create_interpreter("function main() { return 123 + 321; }")
    assert interpreter.run() == 444


def test_interpreter_with_subtraction_expression():
    interpreter = create_interpreter("function main() { return 999 - 453; }")
    assert interpreter.run() == 546


def test_interpreter_with_multiplication_expression():
    interpreter = create_interpreter("function main() { return 23 * 324; }")
    assert interpreter.run() == 7452


def test_interpreter_with_division_expression():
    interpreter = create_interpreter("function main() { return 321 / 3; }")
    assert interpreter.run() == 107


def test_interpreter_with_dividing_by_zero():
    interpreter = create_interpreter("function main() { return 3948 / 0; }")
    with pytest.raises(DivisionError):
        interpreter.run() == 107


def test_interpreter_and_priority_of_multiplication_1():
    interpreter = create_interpreter("function main() { return 23 + 432 * 2; }")
    assert interpreter.run() == 887


def test_interpreter_and_priority_of_multiplication_2():
    interpreter = create_interpreter("function main() { return 89 * 69 + 1; }")
    assert interpreter.run() == 6142

def test_interpreter_and_priority_of_multiplication_3():
    interpreter = create_interpreter("function main() { return 48 * 4 - 12; }")
    assert interpreter.run() == 180


def test_interpreter_and_priority_of_multiplication_4():
    interpreter = create_interpreter("function main() { return 437 - 32 * 9; }")
    assert interpreter.run() == 149


def test_interpreter_and_priority_of_multiplication_5():
    interpreter = create_interpreter("function main() { return 32 * 0; }")
    assert interpreter.run() == 0


def test_interpreter_and_priority_of_multiplication_6():
    interpreter = create_interpreter("function main() { return 32 * -1; }")
    assert interpreter.run() == -32


def test_interpreter_and_priority_of_division_1():
    interpreter = create_interpreter("function main() { return 321 + 432 / 2; }")
    assert interpreter.run() == 537


def test_interpreter_and_priority_of_division_2():
    interpreter = create_interpreter("function main() { return -321 / 3 + 2; }")
    assert interpreter.run() == -105


def test_interpreter_and_priority_of_division_3():
    interpreter = create_interpreter("function main() { return 321 - 432 / 2; }")
    assert interpreter.run() == 105


def test_interpreter_and_priority_of_division_4():
    interpreter = create_interpreter("function main() { return -321 / 3 - 2; }")
    assert interpreter.run() == -109


def test_interpreter_and_priority_of_division_5():
    interpreter = create_interpreter("function main() { return 32 / -2; }")
    assert interpreter.run() == -16


def test_interpreter_with_addition_of_list_and_number():
    interpreter = create_interpreter("function main() { return [12, 32, 755] + 342; }")
    assert interpreter.run() == [12, 32, 755, 342]


def test_interpreter_with_addition_of_number_and_list():
    interpreter = create_interpreter("function main() { return 342 + [12, 32, 755]; }")
    assert interpreter.run() == [342, 12, 32, 755]


def test_interpreter_with_addition_of_empty_list_and_list():
    interpreter = create_interpreter("function main() { return [] + [4, 5, 6]; }")
    assert interpreter.run() == [4, 5, 6]


def test_interpreter_with_addition_of_empty_list_and_number():
    interpreter = create_interpreter("function main() { return [] + 99; }")
    assert interpreter.run() == [99]


def test_interpreter_with_addition_of_empty_list_and_empty_list():
    interpreter = create_interpreter("function main() { return [] + []; }")
    assert interpreter.run() == []


def test_interpreter_with_addition_of_number_and_list_and_number():
    interpreter = create_interpreter("function main() { return 5 + [12, 32, 755] + 342; }")
    assert interpreter.run() == [5, 12, 32, 755, 342]


def test_interpreter_with_addition_of_list_and_list():
    interpreter = create_interpreter("function main() { return [1, 2, 3] + [4, 5, 6]; }")
    assert interpreter.run() == [1, 2, 3, 4, 5, 6]


def test_interpreter_with_addition_of_list_and_true():
    interpreter = create_interpreter("function main() { return [1, 2, 3] + true;}")
    assert interpreter.run() == [1, 2, 3, True]


def test_interpreter_with_addition_of_list_and_false():
    interpreter = create_interpreter("function main() { return [1, 2, 3] + false;}")
    assert interpreter.run() == [1, 2, 3, False]


def test_interpreter_with_addition_of_list_and_variable():
    interpreter = create_interpreter("function main() { number a = 1; return [1, 2, 3] + a;}")
    assert interpreter.run() == [1, 2, 3, 1]


def test_interpreter_with_addition_of_variable_and_list():
    interpreter = create_interpreter("function main() { number a = -2; return a + [1, 2, 3];}")
    assert interpreter.run() == [-2, 1, 2, 3]


def test_interpreter_with_addition_of_variable_and_list():
    interpreter = create_interpreter("function main() { number a = 2; return -a + [1, 2, 3];}")
    assert interpreter.run() == [-2, 1, 2, 3]


def test_interpreter_with_multiplication_of_list_and_number():
    interpreter = create_interpreter("function main() { return [1, 2, 3] * 3;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_number_and_list():
    interpreter = create_interpreter("function main() { return 54 * [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_list_and_bool():
    interpreter = create_interpreter("function main() { return [3, 5, 1, 0] * true;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_bool_and_list():
    interpreter = create_interpreter("function main() { return false * [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_list_and_variable():
    interpreter = create_interpreter("function main() { number a = 3; return [3, 5, 1, 0] * a;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_variable_and_list():
    interpreter = create_interpreter("function main() { number a = 3; return a * [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_multiplication_of_list_and_list():
    interpreter = create_interpreter("function main() { return [] * [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_list_and_number():
    interpreter = create_interpreter("function main() { return [1, 2, 3] - 3;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_number_and_list():
    interpreter = create_interpreter("function main() { return 54 - [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_list_and_bool():
    interpreter = create_interpreter("function main() { return [3, 5, 1, 0] - true;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_bool_and_list():
    interpreter = create_interpreter("function main() { return false - [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_list_and_variable():
    interpreter = create_interpreter("function main() { number a = 3; return [3, 5, 1, 0] - a;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_variable_and_list():
    interpreter = create_interpreter("function main() { number a = 3; return a - [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_list_and_list():
    interpreter = create_interpreter("function main() { return [] - [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_list_and_number():
    interpreter = create_interpreter("function main() { return [1, 2, 3] / 3;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_number_and_list():
    interpreter = create_interpreter("function main() { return 54 / [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_list_and_bool():
    interpreter = create_interpreter("function main() { return [3, 5, 1, 0] / true;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_bool_and_list():
    interpreter = create_interpreter("function main() { return false / [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_list_and_variable():
    interpreter = create_interpreter("function main() { number a = 3; return [3, 5, 1, 0] / a;}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_variable_and_list():
    interpreter = create_interpreter("function main() { number a = 3; return a / [3, 5, 1, 0];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()
        

def test_interpreter_with_division_of_list_and_list():
    interpreter = create_interpreter("function main() { return [] / [1, 2, 3];}")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_minus_list():
    interpreter = create_interpreter("function main() { return -[1, 2, 3]; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_minus_variable():
    interpreter = create_interpreter("function main() { number a = 1; return -a; }")
    assert interpreter.run() == -1


def test_interpreter_with_minus_bool():
    interpreter = create_interpreter("function main() { return -true; }")
    assert interpreter.run() == -1


def test_interpreter_with_minus_number():
    interpreter = create_interpreter("function main() { return -1; }")
    assert interpreter.run() == -1


def test_interpreter_with_undeclared_variable_return():
    interpreter = create_interpreter("function main() { return a; }")
    with pytest.raises(Undeclared):
        interpreter.run()


def test_interpreter_with_undeclared_variable_in_expression():
    interpreter = create_interpreter("function main() { 1 + a; return 3; }")
    with pytest.raises(Undeclared):
        interpreter.run()


def test_interpreter_with_undeclared_variable_in_expression():
    interpreter = create_interpreter("function main() { 1 + a; return 3; }")
    with pytest.raises(Undeclared):
        interpreter.run()

def test_interpreter_with_sum_of_true_and_true():
    interpreter = create_interpreter("function main() { return true + true; }")
    assert interpreter.run() == True


def test_interpreter_with_sum_of_true_and_false():
    interpreter = create_interpreter("function main() { return true + false; }")
    assert interpreter.run() == True


def test_interpreter_with_sum_of_false_and_true():
    interpreter = create_interpreter("function main() { return false + true; }")
    assert interpreter.run() == True


def test_interpreter_with_sum_of_false_and_false():
    interpreter = create_interpreter("function main() { return false + false; }")
    assert interpreter.run() == False


def test_interpreter_with_multiplication_of_true_and_true():
    interpreter = create_interpreter("function main() { return true * true; }")
    assert interpreter.run() == True


def test_interpreter_with_multiplication_of_true_and_false():
    interpreter = create_interpreter("function main() { return true * false; }")
    assert interpreter.run() == False


def test_interpreter_with_multiplication_of_false_and_true():
    interpreter = create_interpreter("function main() { return false * true; }")
    assert interpreter.run() == False


def test_interpreter_with_multiplication_of_false_and_false():
    interpreter = create_interpreter("function main() { return false * false; }")
    assert interpreter.run() == False


def test_interpreter_with_subtraction_of_true_and_false():
    interpreter = create_interpreter("function main() { return true - false; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_false_and_true():
    interpreter = create_interpreter("function main() { return false - true; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_true_and_true():
    interpreter = create_interpreter("function main() { return true - true; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_subtraction_of_false_and_false():
    interpreter = create_interpreter("function main() { return false - false; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_true_and_true():
    interpreter = create_interpreter("function main() { return true / true; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_true_and_false():
    interpreter = create_interpreter("function main() { return true / false; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_false_and_true():
    interpreter = create_interpreter("function main() { return false / true; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()


def test_interpreter_with_division_of_false_and_false():
    interpreter = create_interpreter("function main() { return false / false; }")
    with pytest.raises(UndefinedOperation):
        interpreter.run()

def test_interpreter_with_list_operation_filter_with_single_condition():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x > 6); }")
    assert interpreter.run() == [7, 8, 9]


def test_interpreter_with_list_operation_filter_with_complex_condition():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x > 2 & x < 7); }")
    assert interpreter.run() == [3, 4, 5, 6]


def test_interpreter_with_list_operation_filter_with_GREATER_THAN_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x > 5); }")
    assert interpreter.run() == [6, 7, 8, 9]


def test_interpreter_with_list_operation_filter_with_LESS_THAN_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x < 3); }")
    assert interpreter.run() == [1, 2]


def test_interpreter_with_list_operation_filter_with_GREATER_OR_EQUAL_TO_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x >= 6); }")
    assert interpreter.run() == [6, 7, 8, 9]


def test_interpreter_with_list_operation_filter_with_LESS_OR_EQUAL_TO_to_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x <= 2); }")
    assert interpreter.run() == [1, 2]


def test_interpreter_with_list_operation_filter_with_EQUAL_TO_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x == 7); }")
    assert interpreter.run() == [7]


def test_interpreter_with_list_operation_filter_with_NOT_EQUAL_TO_sign():
    interpreter = create_interpreter("function main() { return [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(x != 7); }")
    assert interpreter.run() == [1, 2, 3, 4, 5, 6, 8, 9]


def test_interpreter_with_list_operation_filter_with_number_instead_of_source_list():
    interpreter = create_interpreter("function main() { number a = 1; return a.filter(x != 7); }")
    with pytest.raises(InvalidOperation):
        interpreter.run()


def test_interpreter_with_list_operation_filter_with_variable_with_list_type():
    interpreter = create_interpreter("function main() { list a = [43, 7, 81]; return a.filter(x != 7); }")
    assert interpreter.run() == [43, 81]


def test_interpreter_with_list_operation_each_with_plus_sign_as_argument():
    interpreter = create_interpreter("function main() { return [1, 2, 3].each(+, 7); }")
    assert interpreter.run() == [8, 9, 10]


def test_interpreter_with_list_operation_each_with_minus_sing_as_argument():
    interpreter = create_interpreter("function main() { return [5, 6, 7].each(-, 6); }")
    assert interpreter.run() == [-1, 0, 1]


def test_interpreter_with_list_operation_each_with_star_sign_as_argument():
    interpreter = create_interpreter("function main() { return [8, 5, 7].each(*, 2); }")
    assert interpreter.run() == [16, 10, 14]


def test_interpreter_with_list_operation_each_with_divide_sign_as_argument():
    interpreter = create_interpreter("function main() { return [8, 6, 20].each(/, 2); }")
    assert interpreter.run() == [4, 3, 10]


def test_interpreter_with_list_operation_each_with_plus_sign_as_argument_and_list():
    interpreter = create_interpreter("function main() { return [8, 6, 20].each(+, [1, 2, 3]); }")
    assert interpreter.run() == [[8, 1, 2, 3], [6, 1, 2, 3], [20, 1, 2, 3]]


#
def test_interpreter_with_list_operation_each_with_plus_sign_and_expression_as_arguments():
    interpreter = create_interpreter("function main() { return [1, 2, 3].each(+, 7 - 3 + 1); }")
    assert interpreter.run() == [6, 7, 8]


def test_interpreter_with_list_operation_each_with_minus_sing_and_expression_as_arguments():
    interpreter = create_interpreter("function main() { return [5, 6, 7].each(-, 6 * 2); }")
    assert interpreter.run() == [-7, -6, -5]


def test_interpreter_with_list_operation_each_with_star_sign_and_expression_as_arguments():
    interpreter = create_interpreter("function main() { return [8, 5, 7].each(*, 2 / 2); }")
    assert interpreter.run() == [8, 5, 7]


def test_interpreter_with_list_operation_each_with_divide_sign_and_expression_as_arguments():
    interpreter = create_interpreter("function main() { return [8, 6, 20].each(/, 1 + 1); }")
    assert interpreter.run() == [4, 3, 10]


def test_interpreter_with_list_operation_each_with_division_by_zero_as_argument():
    interpreter = create_interpreter("function main() { return [8, 6, 20].each(/, 0); }")
    with pytest.raises(DivisionError):
        interpreter.run()


def test_interpreter_with_list_operation_each_with_variable_with_list_type():
    interpreter = create_interpreter("function main() { list a = [43, 7, 81]; return a.each(-, 1); }")
    assert interpreter.run() == [42, 6, 80]


def test_interpreter_with_list_operation_each_with_number_instead_of_source_list():
    interpreter = create_interpreter("function main() { number a = 1; return a.each(+, 17); }")
    with pytest.raises(InvalidOperation):
        interpreter.run()


def test_interpreter_with_list_operation_get_with_number_as_argument():
    interpreter = create_interpreter("function main() { return [9, 8, 7, 6, 5, 4, 3, 2, 1].get(3); }")
    assert interpreter.run() == 6


def test_interpreter_with_list_operation_get_with_variable_as_argument():
    interpreter = create_interpreter("function main() { number a = 6; return [1, 2, 3, 4, 5, 6, 77, 8, 9].get(a); }")
    assert interpreter.run() == 77


def test_interpreter_with_list_operation_get_with_complex_expression_as_argument():
    interpreter = create_interpreter("function main() { number a = 6; return [1, 2, 53, 9, 5, 2, 77, 8, 9].get(1+1*2); }")
    assert interpreter.run() == 9


def test_interpreter_with_list_operation_get_with_negative_number_as_argument():
    interpreter = create_interpreter("function main() { number a = 6; return [1, 2, 53, 9, 5, 2, 77, 8, 9].get(-4); }")
    with pytest.raises(IndexOutOfRange):
        interpreter.run()


def test_interpreter_with_list_operation_get_with_out_of_range_number_as_argument():
    interpreter = create_interpreter("function main() { number a = 6; return [1, 2, 53, 9, 5, 2, 77, 8, 9].get(4354); }")
    with pytest.raises(IndexOutOfRange):
        interpreter.run()


def test_interpreter_with_list_operation_get_with_variable_with_list_type():
    interpreter = create_interpreter("function main() { list a = [43, 7, 81]; return a.get(1); }")
    assert interpreter.run() == 7


def test_interpreter_with_list_operation_get_with_number_instead_of_source_list():
    interpreter = create_interpreter("function main() { number a = 1; return a.get(1); }")
    with pytest.raises(InvalidOperation):
        interpreter.run()


def test_interpreter_with_list_operation_get_with_bool_as_argument():
    interpreter = create_interpreter("function main() { return [3, 2, 1].get(true); }")
    with pytest.raises(InvalidValue):
        interpreter.run()


def test_interpreter_with_list_operation_length_with_simple_list():
    interpreter = create_interpreter("function main() { return [3, 2, 1].length(); }")
    assert interpreter.run() == 3


def test_interpreter_with_list_operation_length_with_empty_list():
    interpreter = create_interpreter("function main() { return [].length(); }")
    assert interpreter.run() == 0


def test_interpreter_with_list_operation_length_with_variable_with_list_type():
    interpreter = create_interpreter("function main() { list a = [43, 7, 81, 2, 0]; return a.length(); }")
    assert interpreter.run() == 5


def test_interpreter_with_list_operation_length_with_number_instead_of_source_list():
    interpreter = create_interpreter("function main() { number a = 1; return a.length(); }")
    with pytest.raises(InvalidOperation):
        interpreter.run()


def test_interpreter_with_list_operation_delete_with_number_as_argument():
    interpreter = create_interpreter("function main() { return [3, 2, 1].delete(1); }")
    assert interpreter.run() == [3, 1]


def test_interpreter_with_list_operation_delete_with_out_of_range_number_as_argument():
    interpreter = create_interpreter("function main() { return [3, 2, 1].delete(50); }")
    assert interpreter.run() == [3, 2, 1]


def test_interpreter_with_list_operation_delete_with_negative_number_as_argument():
    interpreter = create_interpreter("function main() { return [3, 2, 1].delete(-1); }")
    assert interpreter.run() == [3, 2, 1]


def test_interpreter_with_list_operation_delete_with_variable_as_argument():
    interpreter = create_interpreter("function main() { number a = 2; return [3, 2, 1].delete(a); }")
    assert interpreter.run() == [3, 2]


def test_interpreter_with_list_operation_delete_with_bool_as_argument():
    interpreter = create_interpreter("function main() { return [3, 2, 1].delete(true); }")
    with pytest.raises(InvalidValue):
        interpreter.run()


def test_interpreter_with_list_operation_delete_with_variable_with_list_type():
    interpreter = create_interpreter("function main() { list a = [65, 3, 132, 90, 7, 2]; return a.delete(2); }")
    assert interpreter.run() == [65, 3, 90, 7, 2]


def test_interpreter_with_list_operation_delete_with_number_instead_of_source_list():
    interpreter = create_interpreter("function main() { number a = 1; return a.delete(1); }")
    with pytest.raises(InvalidOperation):
        interpreter.run()


def test_interpreter_with_print_operation_with_identifier_as_argument(capsys):
    interpreter = create_interpreter("function main() { number a = 43317; print a; }")
    interpreter.run()
    out, _ = capsys.readouterr()
    assert out == "43317\n"


def test_interpreter_with_print_operation_with_number_as_argument(capsys):
    interpreter = create_interpreter("function main() { print 1; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()


def test_interpreter_with_print_operation_with_bool_as_argument(capsys):
    interpreter = create_interpreter("function main() { print true; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()


def test_interpreter_with_print_operation_with_list_as_argument(capsys):
    interpreter = create_interpreter("function main() { print [1, 2, 3, 4, 5]; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()


def test_interpreter_with_print_operation_with_expression_as_argument(capsys):
    interpreter = create_interpreter("function main() { print 1 + 1; }")
    with pytest.raises(InvalidSyntax):
        interpreter.run()