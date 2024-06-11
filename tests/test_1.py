from miu import *
import pytest


#def test_variable():
#    assert axiom == "mi", "Expect axiom to be \"mi\""


def test_first_rule():
    
    assert first_rule(
        previous_theorem) == "miu", "Expect first theorem to be \"miu\""

def test_second_rule():

    assert second_rule(previous_theorem) == "mii", "Expect 'mi' is 'mii' after second_rule is been used over it."

@pytest.mark.parametrize(
    "input_str, expected_output_str", [('miii', 'mu')]
)
def test_third_rule(input_str, expected_output_str):

    assert third_rule(input_str) == expected_output_str, "Expect 'miii' is 'mu' after third_rule() is been used over it."

#test_first_rule()
#test_second_rule()
#test_third_rule()
