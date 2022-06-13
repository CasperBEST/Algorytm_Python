"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""


import random
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
    # print(matrix)
    sum_1 = 0
    sum_1 += sys.getsizeof(matrix)
    sum_1 += sys.getsizeof(temp_array)
    sum_1 += sys.getsizeof(i)
    sum_1 += sys.getsizeof(range)
    print(f'Переменные в первом алгоритме занимают {sum_1} байт.')


# 2. Создание матрицы с помощью двух циклов:

def matrix_create_2_cycle(raw, coll):
    matrix = [[random.randint(1, 100) for i in range(1, coll)] for _ in range(1, raw)]
    sum_2 = sys.getsizeof(matrix)
    print(f'Переменные во втором алгоритме занимают {sum_2} байт.')


matrix_create_1_cycle(100)
matrix_create_2_cycle(100, 100)

"""
Версия питона - 3.10
Система - 64-разрядная
Для подсчета используем алгоритмы создания матриц с одним и двумя циклами.
Для создания матрицы 100х100 в первом случае переменные занимают 1412 байт, а во втором 920 байт.
Соответственно алгоритм с двумя циклами наиюолее эффективно использует память.
"""