from miu import *
import pytest

def test_simple_order():
    axiom = 'mi'
    previous_theorem = axiom
    
    previous_theorem = first_rule(previous_theorem)
    previous_theorem = second_rule(previous_theorem)
    previous_theorem = third_rule(previous_theorem)
    previous_theorem = fourth_rule(previous_theorem)

    assert previous_theorem == 'miuiu', "После применения четырёх правил строка 'mi' должна стать 'miuiu'."


# 
def test_func_bunch():
    axiom = 'mi'
    previous_theorem = axiom
    func_bunch = [first_rule, second_rule, third_rule, fourth_rule]
    for f in func_bunch:
        previous_theorem = f(previous_theorem)
    
    assert previous_theorem == 'miuiu', "После применения func_bunch() строка 'mi' должна стать 'miuiu'."
