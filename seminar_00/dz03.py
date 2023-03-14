# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

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
    
choclate_lenght = prompt('Введите длину шоколадки, в дольках')
choclate_wide = prompt('Введите ширину шоколадки, в дольках')
peace = prompt('Введите количество долек, которое хотите отломить')

peace_1 = peace % choclate_lenght
peace_2 = peace % choclate_wide

if peace_1 == 0:
    print('Так можно отломить кусочек')
elif peace_2 == 0 and peace != choclate_lenght * choclate_wide:
    print('Так тоже можно отломить кусочек')
else:
    print('А вот так не нужно ломать')