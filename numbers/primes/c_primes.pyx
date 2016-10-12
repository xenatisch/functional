from libc.math cimport sqrt
from Primes.py_primes import extend_with_none
cimport cython

ctypedef unsigned int uint;
ctypedef unsigned long ulong;
ctypedef unsigned long long int ul_long;
ctypedef unsigned short ushort;

# @cython.boundscheck(False)
cpdef primes(const ulong num):
    """
    Get a list of a desired count of prime numbers.
    :param num: Number of prime numbers (N).
    :type num: short, int, long
    :return: List of prime numbers, readable in Python.
    :rtype: list

    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    cdef ulong iterator;

    primes_list = [0]*num

    # In case of memory stack overflow.
    if not primes_list:
        raise MemoryError()

    cdef uint k = 0;
    cdef uint n = 2;

    while k < num:
        if _is_prime(n):
            primes_list[k] = n
            k += 1
        n += 1

    return primes_list


cdef _is_prime(const ul_long num):
    if num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False

    cdef ushort increment_by = 6;
    cdef long double sq = sqrt(num);
    cdef ulong iterator = 5;

    while iterator <= sq:
        if num % iterator == 0 or num % (iterator + 2) == 0:
            return False
        iterator += increment_by

    return True


def is_prime(const ulong num):
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
    return _is_prime(num)

# @cython.boundscheck(False)
cpdef primes_to(const ulong num_max):
    """
    Get a list of prime numbers ranging from zero to the desired natural number (N).
    :param num_max: Maximum search limit.
    :type num_max: short, int, long
    :return: List of prime numbers to the desired maximum, readable in Python.
    :rtype: list

    >>> primes_to(10)
    [2, 3, 5, 7]
    """
    primes_list = [None] * 1000

    cdef ulong iterator = 2, iter_found = 0;

    while iterator <= num_max:
        if _is_prime(iterator):
            try:
                primes_list[iter_found] = iterator
            except IndexError:
                primes_list = extend_with_none(primes_list)
                primes_list[iter_found] = iterator

            iter_found += 1
        iterator += 1

    return list(filter(None, primes_list))

