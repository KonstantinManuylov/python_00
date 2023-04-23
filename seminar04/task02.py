# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

number = int(input('Введите число > '))

def define(num:int) -> bool:
    """Проверяет, является ли число простым"""
    if num == 2:
        return True
    elif num % 1 == 0 and num % num == 0 and num % 2 != 0:
        return True
    else:
        return False
    
print(define(number))