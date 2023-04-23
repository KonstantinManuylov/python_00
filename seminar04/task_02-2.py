num = int(input("Введите число: "))

def define_simple(num: int): 
    for i in range(2, num // 2+1):
        if (num % i == 0):
            return "Число не является простым"
    return "Число простое"

print(define_simple(num))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(num))


def is_prime_recurs(number, divisor=2):
    if number < 2:
        return False
    if divisor > int(number**0.5):
        return True
    if number % divisor == 0:
        return False
    return is_prime_recurs(number, divisor + 1)

print(is_prime_recurs(num))