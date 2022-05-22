# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random


matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(10)])

min_list = []
min_list.extend(matrix[0])

for s in matrix:
    print()
    print(('{:4d} ' * len(s)).format(*s))
    i = 0
    for j in s:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print('Список минимальных элементов столбцов матрицы:')
print(('{:4d} ' * len(min_list)).format(*min_list))

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_list[0])
