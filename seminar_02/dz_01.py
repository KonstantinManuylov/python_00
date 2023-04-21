# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

list_length = int(input('Введите длину списка > '))
numbers_list = [randint(0, 10) for i in range(list_length)]
x = int(input('Введите искомое значение > '))

print(f'Список рандомных чисел:\n{numbers_list}')

min_difference = numbers_list[0]

for i in numbers_list:
    differ = abs(i - x)
    if differ < min_difference:
        result = i
        min_difference = differ

print(f'Ближайшее по значению число {result}')