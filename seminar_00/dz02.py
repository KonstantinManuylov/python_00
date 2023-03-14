# счастливый билетик
# 385916 -> yes
# 123456 -> no

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
            if int(len(number)) < 1 or int(len(number)) > 6:
                return prompt('Вы ввели некоректное значение. Введите еще раз')
            else:
                return number
    else:
        return prompt('Вы ввели некоректное значение. Введите еще раз')

def find_left_side_sum(number: int):
    number = number // 1000
    sum = 0
    while number != 0:
        left = number % 10
        number = number // 10
        sum = sum + left
    return sum

def find_right_side_sum(number: int):
    number = number % 1000
    sum = 0
    while number != 0:
        left = number % 10
        number = number // 10
        sum = sum + left
    return sum

ticket = prompt('Введите номер билета')
left_side = find_left_side_sum(int(ticket))
rigth_side = find_right_side_sum(int(ticket))
if left_side == rigth_side:
    print('Поздравляем! Билет счастливый!')
else:
    print('Билет несчасливый :(. Купите еще билетик, может повезет.')