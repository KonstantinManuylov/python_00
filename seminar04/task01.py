# Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

marks = [1, 3, 5, 3, 3, 4, 5]
MAX_MARK = 5
MIN_MARK = 1

def change_marks(numbers: list[int]) -> list[int]:
    """Заменяет пятерки на единицы"""
    for i in range(len(numbers)):
        if numbers[i] == MAX_MARK:
            numbers[i] = MIN_MARK
    return numbers

# result = [i if i != max else min for i in marks]

result_list = change_marks(marks)
print(result_list)