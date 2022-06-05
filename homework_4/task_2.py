# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


import cProfile

#  1. Решето Эратосфена:


def eratosthenes(number):
    if number < 600:
        last_index = (number // 20) * 150
    elif number < 600000:
        last_index = (number // 20) * 300
    else:
        last_index = (number // 20) * 500

    sieve = [i for i in range(last_index)]

    sieve[1] = 0

    for i in range(2, last_index):
        if sieve[i] != 0:
            j = i * 2
            while j < last_index:
                sieve[j] = 0
                j += i

    sieve_number = [i for i in sieve if i != 0]
    print(f'{number} по счету простое число равно {sieve_number[number - 1]}')


# cProfile.run('eratosthenes(100)')
# 1    0.000    0.000    0.000    0.000 task_2.py:11(eratosthenes)

# cProfile.run('eratosthenes(500)')
# 1    0.001    0.001    0.002    0.002 task_2.py:11(eratosthenes)

# cProfile.run('eratosthenes(1000)')
# 1    0.014    0.014    0.015    0.015 task_2.py:11(eratosthenes)

# cProfile.run('eratosthenes(100000)')
# 1    0.893    0.893    1.041    1.041 task_2.py:11(eratosthenes)

# cProfile.run('eratosthenes(500000)')
# 1    4.527    4.527    5.263    5.263 task_2.py:11(eratosthenes)


# 2. Свой вариант:


def get_right_number(number):
    num = 3
    right_number = [2]
    nums = [2]
    while True:
        if len(right_number) == number:
            print(f'{number} по счету простое число равно {right_number[number - 1]}')
            break
        else:
            for i in nums:
                if num % i == 0:
                    nums.append(num)
                    break
            else:
                nums.append(num)
                right_number.append(num)
        num += 1


# cProfile.run('get_right_number(100)')
# 1    0.002    0.002    0.002    0.002 task_2.py:53(get_right_number)

# cProfile.run('get_right_number(500)')
# 1    0.060    0.060    0.060    0.060 task_2.py:53(get_right_number)

# cProfile.run('get_right_number(1000)')
# 1    0.301    0.301    0.303    0.303 task_2.py:53(get_right_number)

# cProfile.run('get_right_number(5000)')
# 1    9.886    9.886    9.903    9.903 task_2.py:53(get_right_number)


# Алгоритм с использованием решета Эратосфена работает гораздо быстрее!
