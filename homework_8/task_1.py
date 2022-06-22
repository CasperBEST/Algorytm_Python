"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


import hashlib


def substring_count(string):
    string = str(string).lower()
    hash_set = set()
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            hash_string = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(hash_string)
    return len(hash_set)


some_string = 'hello world'

print(f'Количество различных подстрок в строке "{some_string}": {substring_count(some_string)}')
