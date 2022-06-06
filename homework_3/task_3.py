# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import randint


my_array = [randint(0, 99) for _ in range(10)]
print(f'Массив до изменений:\n{my_array}')

maxi = my_array[0]
mini = my_array[0]

for i in my_array:
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i

min_index = my_array.index(mini)
max_index = my_array.index(maxi)
my_array[min_index], my_array[max_index] = my_array[max_index], my_array[min_index]

print(f'Минимальный и максимальный элементы массива: {mini} и {maxi}')
print(f'Массив после изменений:\n{my_array}')
