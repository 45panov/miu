"""
    Эта программа решает задачу преобразования строки 'mi' в строку 'mu'. 
    К исходной строке можно применять одно из трёх правил. 1) Если строка
    кончается на 'i', к ней можно добавить 'u' в конце. 2) Если имеется mx
    (где х - любая строка), то к ней можно добавить 'mxx'. 3) Если в строке 
    встречается 'iii', её можно заменить на 'u'.

"""
import re

def next_theorem(previous_theorem, rule):
    return re.sub(rule, "iu", previous_theorem)

if __name__ == '__main__':
    axiom = "mi" # Source string
    pattern_of_rule = r'i$'
    print(next_theorem(axiom, pattern_of_rule))
