# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def get_sum(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum


my_numbers = [i for i in input('Введите натуральные числа через пробел: ').split()]

number = 0
max_sum = 0

for i in my_numbers:
    if get_sum(i) > max_sum:
        number = i
        max_sum = get_sum(i)
print(f'У числа {number} максимальная сумма цифр {max_sum}')
