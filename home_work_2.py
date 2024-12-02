#  Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]






#
# def find_indices_in_range(arr, min_val, max_val):
#     ind = []
#     for i, value in enumerate(arr):
#         if min_val <= value <= max_val:
#             ind.append(i)
#         return ind
#
# array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#
# min_value = -2
# max_value = 4
#
# result = find_indices_in_range(array, min_value, max_value)
# print(result)


def find_indices_in_range(arr, min_val, max_val):
    """Находит индексы элементов массива, находящихся в заданном диапазоне."""
    indices = []  # Список для хранения индексов

    for i, value in enumerate(arr):
        if min_val <= value <= max_val:
            indices.append(i)

    return indices


# Исходный массив
array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Границы диапазона
min_value = -2
max_value = 4

# Находим индексы элементов, принадлежащих диапазону
result = find_indices_in_range(array, min_value, max_value)

# Вывод результата
print(result)