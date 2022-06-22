"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


import random


# Алгоритм сортировки слиянием состоит из двух частей. Первая рекурсивно делит массив пополам и вторая,
# которая объединяет две половины, создавая отсортированный массив.


def merge(left, right):
    """
    Функция объединяет две половины, создавая отсортированный массив
    """
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    """
    Функция рекурсивно разбивает входные данные пополам
    """
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


my_list = [random.randint(0, 50) for i in range(15)]
print(f'Исходный массив:        {my_list}')
print(f'Отсортированный массив: {merge_sort(my_list)}')
