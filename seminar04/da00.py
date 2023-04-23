# Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

base_num = int(input('Введите базовое значение > '))
pow_num = int(input('Введите значение степени > '))

def find_pow(base: int, pow: int) -> int:
    """вычисляет возведение в степень рекурсией"""
    if pow == 0:
        return 1
    return base * find_pow(base, pow - 1)

print(f'Результат: {base_num} в степени {pow_num} = {find_pow(base_num, pow_num)}')