#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python:
# None

# 3rd party:
from pyximport import install; install()  # Cython package. 

# Internal:
from numbers.primes import c_primes, py_primes

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'GPLv.2'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '07/05/2016, 22:41'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# start = time()
c_p = c_primes.primes_to(10000000)
# stop = time() - start
print(len(c_p))

# start = time()
p_p = py_primes.primes_to(1000000)
# stop = time() - start
print(len(p_p))
# print(len(c_p), c_p[-1])
# p_p = py_primes.primes(1000)
# print(len(p_p), p_p[-1])
