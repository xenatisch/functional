#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

try:
    # 3rd party:
    from numpy import sqrt
except ImportError:
    # Python:
    from math import sqrt


# Internal:
# None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'GPLv.2'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '09/05/2016, 11:59'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def extend_with_zero(item): return item + [0] * len(item)


def extend_with_none(item): return item + [None] * len(item)


def extend_with_x(item, x): return item + [x] * len(item)


def primes(num):
    """
    Get a list of a desired count of prime numbers.
    :param num: Number of prime numbers (N).
    :type num: short, int, long
    :return: List of prime numbers, readable in Python.
    :rtype: list

    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    prime_list = [0]*num
    k = 0
    n = 2

    while k < num:
        iterator = 0
        while iterator < k and n % prime_list[iterator] != 0:
            iterator += 1

        if iterator == k:
            prime_list[k] = n
            k += 1

        n += 1

    return prime_list


def is_prime(num):
    """
    Check if a natural (N) number is prime.
    :param num: The number to be checked.
    :type num: short, int, long
    :return: True if the number is prime, otherwise False.
    :rtype: Bool

    >>> is_prime(10)
    False

    >>> is_prime(7)
    True
    """
    if num <= 3:
        return num > 1

    elif num % 2 == 0 or num % 3 == 0:
        return False

    increment_by = 6
    sq = sqrt(num)
    iterator = 5

    while iterator <= sq:
        if num % iterator == 0 or num % (iterator + 2) == 0:
            return False

        iterator += increment_by

    return True


def primes_to(num_max):
    """
    Get a list of prime numbers ranging from zero to the desired natural number (N).
    :param num_max: Maximum search limit.
    :type num_max: short, int, long
    :return: List of prime numbers to the desired maximum, readable in Python.
    :rtype: list

    >>> primes_to(10)
    [2, 3, 5, 7]
    """
    primes_list = [None]*1000  # Python list

    iterator = 0
    iter_found = 0

    while iterator <= num_max:
        if is_prime(iterator):
            try:
                primes_list[iter_found] = iterator
            except IndexError:
                primes_list = extend_with_none(primes_list)
                primes_list[iter_found] = iterator

            iter_found += 1

        iterator += 1

    return list(filter(None, primes_list))


if __name__ == '__main__':
    import doctest
    test_res = doctest.testmod()
