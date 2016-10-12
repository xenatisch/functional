#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python:

# 3rd party:
from math import fsum
# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '01/05/2016, 12:26'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_pi(precision):
    """
    Calculate the value of Pi to the specified precision. Note: It's not generally a good idea to attempt precisions
    greater than 1e9 unless you're using a very powerful computer and are prepared to wait.
    :param precision: Precision of Pi.
    :type precision: int
    :return: Pi calculated to the requested precision.
    :rtype: float

    >>> pi = get_pi(1000000)
    >>> print(pi)
    3.1415926535898766
    """
    assert(isinstance(precision, int))

    delta = 1 / precision
    dlt = 4 * (1 / precision)
    arr = (dlt * (1 / (1 + ((val - .5) * delta) ** 2)) for val in range(1, int(precision) + 1))
    pi = fsum(arr)

    return pi


if __name__ == "__main__":
    import doctest
    test_res = doctest.testmod()
