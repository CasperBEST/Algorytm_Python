# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


while True:
    try:
        number = int(input('Введите натуральное число: '))
    except ValueError:
        print('Введено неверное значение.')
        break
    even_numbers = 0
    odd_numbers = 0
    for i in str(number):
        if int(i) % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    print(f'Число {number} содержит {even_numbers} четных и {odd_numbers} нечетных чифры.')
    break


