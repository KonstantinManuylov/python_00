def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input('Введите число > '))
print(fibonacci(number - 2))

for i in range(2, number + 1):
    print(fibonacci(i - 2))