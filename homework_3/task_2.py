# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если
# индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint


array_1 = [randint(0, 99) for _ in range(10)]
array_2 = []

for n in range(len(array_1)):
    if array_1[n] % 2 == 0:
        array_2.append(n)
print(f'Массив 1 - {array_1}\nМассив из индексов четных элементов первого массива - {array_2}')
