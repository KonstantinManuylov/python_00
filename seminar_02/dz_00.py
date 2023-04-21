# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    3
#    -> 1

import random

# def find_number_value(num_list:list, number:int):
#     count = 0
#     for i in range(0, num_list):
 #        if number == num_list[i]:
#             count += 1
#     return count

last_number = int(input('Введите какого размера будет список > '))
numbers_list = [random.randint(0, 5) for _ in range(last_number)]
searching_number = int(input('Какое число ищем? > '))

print(numbers_list)

result = numbers_list.count(searching_number)

print(f'Число {searching_number} встречается в списке {result} раз.')