# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.


# Попробуем сравнить разные алгоритмы создания матриц.


import random
import cProfile
import sys


# 1. Создание матрицы с помощью одного цикла:

def matrix_create_1_cycle(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        number = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(number)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(number)
    print(matrix)


# cProfile.run("matrix_create_1_cycle(10)")
# 1    0.000    0.000    0.001    0.001 task_1.py:16(matrix_create_1_cycle)

# cProfile.run("matrix_create_1_cycle(100)")
# 1    0.007    0.007    0.051    0.051 task_1.py:16(matrix_create_1_cycle)

# cProfile.run("matrix_create_1_cycle(1000)")
# 1    0.755    0.755    4.182    4.182 task_1.py:16(matrix_create_1_cycle)


# 2. Создание матрицы с помощью двух циклов:

def matrix_create_2_cycle(raw, coll):
    matrix = [[random.randint(1, 100) for _ in range(1, coll)] for _ in range(1, raw)]


# cProfile.run('matrix_create_2_cycle(10, 10)')
# 1    0.000    0.000    0.000    0.000 task_1.py:16(matrix_create_1_cycle)

# cProfile.run('matrix_create_2_cycle(100, 100)')
# 1    0.000    0.000    0.032    0.032 task_1.py:16(matrix_create_2_cycle)

# cProfile.run('matrix_create_2_cycle(1000, 1000)')
# 1    0.000    0.000    3.478    3.478 task_1.py:16(matrix_create_2_cycle)


# 3. Создание матрицы с помощью рекурсии:

sys.setrecursionlimit(2000)


def matrix_create_recursion(raw, coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == coll:
        for _ in range(raw):
            matrix.append(random.randint(1, 100))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(raw):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        f_matrix = matrix_create_recursion(raw, coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix


# cProfile.run('matrix_create_recursion(10, 10)')
# 10/1    0.000    0.000    0.000    0.000 task_1.py:63(matrix_create_recursion)

# cProfile.run('matrix_create_recursion(100, 100)')
# 100/1    0.011    0.000    0.048    0.048 task_1.py:63(matrix_create_recursion)

# cProfile.run('matrix_create_recursion(1000, 1000)')
# 1000/1    0.645    0.001    4.008    4.008 task_1.py:63(matrix_create_recursion)

# Итог:
# Сложность всех алгоритмов О(N**2), но скорость работы лучше у алгоритма с двумя циклами. К тому же при создании
# больших матриц, с помощью рекурсии, необходимо увеличивать размер стека. Иначе программа не закончит свою работу.
#
# В результате алгоритм с двумя циклами быстрее и удобнее в работе.

