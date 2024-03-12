"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    res = []
    for num in nums:
        res.append(num ** 2)

    return res


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, (n // 2)+1):
        if n % i == 0:
            return False
    return True


def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


def filter_numbers(nums, arg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    res = []
    if arg == 'prime':
        res = filter(is_prime, nums)
        return list(res)

    if arg == 'odd':
        res = filter(is_odd, nums)
        return list(res)

    if arg == 'even':
        res = filter(lambda n: n % 2 == 0, nums)
        return list(res)

