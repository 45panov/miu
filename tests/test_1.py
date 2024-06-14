from miu import *
import pytest


# Тест Правила №1 (Если у вас есть строчка, кончающаяся на i, вы можете
# прибавить u в конце.)

@pytest.mark.parametrize(
    "input_str, expected_output_str", [('mi', 'miu'),
                                       ('muiu', 'muiu')]
)
def test_first_rule(input_str, expected_output_str):

    assert first_rule(
        input_str) == expected_output_str, "Если у вас есть строчка, кончающаяся на i, вы можете прибавить u в конце."


# Тест Правила №2 (Если у вас имеется mx, вы можете прибавить mxx).

@pytest.mark.parametrize(
    "input_str, expected_output_str", [('mi', 'mii'),
                                       ('mmuu', 'mmuuuu'),
                                       ('mm', 'mmm')]
)
def test_second_rule(input_str, expected_output_str):

    assert second_rule(
        input_str) == expected_output_str, "Если у вас имеется mx, вы можете прибавить mxx."


# Тест Правила №3 (Если у вас в строчке имеется iii, вы можете заменить его на
# u).

@pytest.mark.parametrize(
    "input_str, expected_output_str", [('miii', 'mu'),
                                       ('miiiummiuuuiiimmm', 'muummiuuuummm')]
)
def test_third_rule(input_str, expected_output_str):

    assert third_rule(
        input_str) == expected_output_str, "Expect 'miii' is 'mu' after third_rule() is been used over it."


# Тест правила №4 (Если у вас есть uu, вы можете её опустить).

@pytest.mark.parametrize(
    "input_str, expected_output_str", [('muu', 'm'),
                                       ('miuuiimuu', 'miiim')]
)
def test_fourth_rule(input_str, expected_output_str):

    assert fourth_rule(
        input_str) == expected_output_str, "Expect 'miii' is 'mu' after third_rule() is been used over it."
