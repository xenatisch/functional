#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Cython/C:

# Python:

# 3rd party:

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Author: Pouria Hadjibagheri
Copyright: Copyright 2016
Credits: Pouria Hadjibagheri
Licence: MIT
Maintainer: Pouria Hadjibagheri
Email: p.bagheri.12@ucl.ac.uk
Created on: 11/05/2016, 18:16
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cpdef get_pi(precision):
    assert(isinstance(precision, int) and precision>0)
    cdef long double prec = precision;
    cdef long double delta = 1 / prec;
    cdef long double dlt = 4 * (1 / prec);

    cdef long double iterator = 0;

    cdef long double sum_pi = 0;

    while iterator <= prec:
        sum_pi += (dlt * (1 / (1 + ((iterator - .5) * delta) ** 2)))
        iterator += 1
    return sum_pi

