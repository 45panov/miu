"""
    Эта программа решает задачу преобразования строки 'mi' в строку 'mu'. 
    К исходной строке можно применять одно из трёх правил. 1) Если строка
    кончается на 'i', к ней можно добавить 'u' в конце. 2) Если имеется mx
    (где х - любая строка), то к ней можно добавить 'mxx'. 3) Если в строке 
    встречается 'iii', её можно заменить на 'u'.

"""
from re import sub, search
from itertools import product
axiom = 'mi'
previous_theorem = axiom

def first_rule(income_str):
    return sub(r'i$', 'iu', income_str)

def second_rule(income_str):
    res = search(r'[ui]*[uim]$', income_str)
    return income_str + res.group(0)

def third_rule(income_str):
    return sub('iii', 'u', income_str)

def fourth_rule(income_str):
    return sub('uu', '', income_str)

if __name__ == "__main__.py":
    pass
