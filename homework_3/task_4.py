# Определить, какое число в массиве встречается чаще всего.


from random import randint


my_array = [randint(0, 9) for _ in range(100)]
print(my_array)

number = 0

for i in my_array:
    if my_array.count(number) < my_array.count(i):
        number = my_array.index(i)

print(f'Число {my_array[number]} в массиве втречается {my_array.count(number)} раз(а)')
