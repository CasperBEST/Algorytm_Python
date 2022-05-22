# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


from random import randint


my_array = [randint(0, 100) for _ in range(50)]
print(f'Массив {my_array}')

min_1 = 0
min_2 = 1

for i in my_array:
    if my_array[min_1] > i:
        min_2 = min_1
        min_1 = my_array.index(i)
    elif my_array[min_2] > i:
        min_2 = my_array.index(i)

print(f'Два наименьших элемента: {my_array[min_1]} и {my_array[min_2]}')

# # Второй способ через сортировку списка
#
# sort_list = []
# sort_list.extend(my_array)
# sort_list.sort()
#
# print(f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}')
