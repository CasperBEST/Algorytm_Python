"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""


import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


my_list = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный массив:        {my_list}')
print(f'Отсортированный массив: {bubble_sort(my_list)}')
