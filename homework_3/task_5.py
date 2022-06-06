# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


from random import randint


my_array = [randint(-100, 100) for _ in range(20)]
print(my_array)

number = 0

for i in my_array:
    if i < number:
        number = i

if number == 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимальный отрицательный элемент массива: {number} находится на {my_array.index(number)} позиции.')
