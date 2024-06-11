"""
    Эта программа решает задачу преобразования строки 'mi' в строку 'mu'. 
    К исходной строке можно применять одно из трёх правил. 1) Если строка
    кончается на 'i', к ней можно добавить 'u' в конце. 2) Если имеется mx
    (где х - любая строка), то к ней можно добавить 'mxx'. 3) Если в строке 
    встречается 'iii', её можно заменить на 'u'.

"""
import re

axiom = 'mi'
previous_theorem = axiom
#frst_rule = {'pattern': r'i$', 'repl': 'iu'}
#scnd_rule = {'pattern': r'[ui]*[uim]$', }
#
#def next_theorem(rule: dict, previous_theorem: str):
#    return re.sub(rule['pattern'], rule['repl'], previous_theorem)

def first_rule(income_str):
    return re.sub(r'i$', 'iu', income_str)

def second_rule(income_str):
    res = re.search(r'[ui]*[uim]$', income_str)
    return income_str + res.group(0)

def third_rule(income_str):
    return re.sub('iii', 'u', income_str)
