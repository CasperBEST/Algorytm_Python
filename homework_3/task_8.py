# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


matrix = []

print('Создаем матрицу 5х4')
for i in range(4):
    matrix.append([])
    sum = 0
    for n in range(4):
        user_input = int(input(f'Введите элемент {i + 1} из {n + 1} столбца: '))
        sum += user_input
        matrix[i].append(user_input)

    matrix[i].append(sum)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
