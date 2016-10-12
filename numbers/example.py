#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python:
import time

# 3rd party:
from pyximport import install; install()  # Cython package.

# Internal:
import c_pi
import numbers.pi as pir

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '11/05/2016, 18:29'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tic = time.clock()
pi = c_pi.get_pi(100000)
toc = time.clock()

print('Calculated {} in {:3g} seconds.'.format(pi, toc-tic))

tic = time.clock()
pir.get_pi(100000)
toc = time.clock()

print('Calculated {} in {:3g} seconds.'.format(pi, toc-tic))
