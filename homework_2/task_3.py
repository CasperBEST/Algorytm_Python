# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


number = input('Введите число: ')
for i in number:
    if i.isdigit() is not True:
        raise ValueError('Число должно быть только из цифр')

print(''.join(reversed(number)))
