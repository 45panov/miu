from miu import *
import pytest


#def test_variable():
#    assert axiom == "mi", "Expect axiom to be \"mi\""


def test_first_rule():
    assert next_theorem(
        'mi', r'i$') == "miu", "Expect first theorem to be \"miu\""


test_first_rule()
#test_variable()
