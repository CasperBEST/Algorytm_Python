# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


my_sequence = input('Введите последовательность чисел: ')
for i in my_sequence:
    if i.isdigit() is not True:
        raise ValueError('Допускаются только цифры')
my_number = input('Введите цифру: ')
if my_number.isdigit() is not True or len(my_number) != 1:
    raise ValueError('Допускается только цифра')

n = 0
for i in my_sequence:
    if i == my_number:
        n += 1
print(f'В данной последовательноти цифра {my_number} встречается {n} раз.')

