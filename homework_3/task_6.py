# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


from random import randint


my_array = [randint(0, 100) for _ in range(10)]
print(f'Массив {my_array}')

min_i = 0
max_i = 0
step = 1
sum = 0

for i in my_array:
    if my_array[min_i] > i:
        min_i = my_array.index(i)
    elif my_array[max_i] < i:
        max_i = my_array.index(i)

if max_i - min_i < 0:
    step = -1

for i in my_array[min_i + step:max_i:step]:
    sum += i
    # print(f'DEBUG i={i}')

print(
        f'Сумма элементов массива между минимальным ({my_array[min_i]})',
        f' и максимальным ({my_array[max_i]}) элементами: {sum}'
        )
