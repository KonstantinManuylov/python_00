# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def prompt(message: str):
    number = input(message + ' > ')
    if isint(number) == True:
        while True:
            if int(number) < 100 or int(number) > 999:
                return prompt('Вы ввели некорректное значение, введите трехзначное число')
            else:
                return number
    else:
        return prompt('Вы ввели некорректное значение, введите трехзначное число')

def count_sum_numbers(number: int):
    left = 0
    sum = 0
    while number != 0:
        left = int(number) % 10
        number = int(number) // 10
        sum = sum + left
    return sum

number = prompt('Введите трехзначное число')
result = count_sum_numbers(number)
print(f'сумма цифр в числе {number} = {result}')