def print_operation_table(operation, num_rows=6, num_columns=6):
    # Вывод заголовка таблицы
    print('{:>4}'.format(''), end='')
    for col in range(1, num_columns + 1):
        print('{:>8}'.format('col ' + str(col)), end='')
    print()

    # Вывод строк таблицы с результатами вычислений
    for row in range(1, num_rows + 1):
        print('{:>4}'.format('row ' + str(row)), end='')
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print('{:>8}'.format(result), end='')
        print()

print(print_operation_table(lambda x, y: x * y, num_rows=10, num_columns=10))