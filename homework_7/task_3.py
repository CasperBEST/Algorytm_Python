"""
 Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
 медианы, в другой – не больше медианы.
"""

import random


def median_search(array, first, last):

    array = array.copy()
    idx = len(array) // 2

    if first >= last:
        return array[idx]

    pillar = array[idx]
    a = first
    z = last

    while a <= z:

        while array[a] < pillar:
            a += 1

        while array[z] > pillar:
            z -= 1

        if a <= z:
            array[a], array[z] = array[z], array[a]
            a += 1
            z -= 1

    if idx < a:
        array[idx] = median_search(array, first, z)

    elif z < idx:
        array[idx] = median_search(array, a, last)

    return array[idx]


m = random.randint(1, 20)
size = 2 * m + 1

my_array = [random.randint(-100, 100) for _ in range(size)]

print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', my_array, sep='\n')

median = median_search(my_array, 0, len(my_array) - 1)
print(f'Медиана: {median}')


print('\nПроверка:')
my_array.sort()
print(f'Отсортированный массив: {my_array}')
print(f'Мкдиана {my_array[len(my_array) // 2]}')
