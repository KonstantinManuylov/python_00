# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def prompt(message: str):
    number = input(message + ' > ')
    if isint(number) == True:
        return int(number)
    else:
        return prompt('Вы ввели некорректное значение, введите число')

def left_papers(num: int):
    left = num % 6
    return left

def find_result(num: int):
    result = []
    petiya = num // 6
    sergey = num // 6
    katya = (petiya + sergey) * 2
    result.append(petiya)
    result.append(sergey)
    result.append(katya)
    return result

value = prompt('Введите общее количество журавликов')
left = left_papers(value)
result_list = find_result(value)
print(f'Петя = {result_list[0]} \nКатя = {result_list[1]} \nСургей = {result_list[2]}')
if left > 0:
    print(f'А этих {left} журавликов сделал человек-Невидимка :-)')