#!/usr/bin/env python3

"""
Functions for converting string values containing numbers, or an iterable containing such
values to floating point or integer numbers (or a similar type of array of floating points
or integer numbers).

Programmed in Python 3.5.2-final.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri@ucl.ac.uk'
__date__ = '12/10/2016, 19:22'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def str2float(value):
    """
    Converts numeric values from `str` or an array thereof to `float`.

    If numeric value is in the correct format, but contains invalid
    characters entered by mistake, such mistakes are automatically discarded.
    _Note_: Existence of `E` or `e` in the number is regarded as exponent, not
    a mistake.

    :param value: `str` or an array thereof containing numeric values.
    :type value: str, list, tuple, set
    :return: `float`, or an array of `float` numbers in the same type as the one given.
    :rtype: float, list, tuple, set

    >>> value = '3.4'
    >>> str2float(value)
    3.4

    >>> value = '3.4cvb'
    >>> str2float(value)
    3.4

    >>> value_list = {'3.4', '5.6'}
    >>> str2float(value_list)
    {3.4, 5.6}

    Timing for this example: 10000 loops, best of 3: 25.6 µs per loop
    >>> value_list = ['5.3fs', '-5e4', '6.8', '3e16', '19.1rgf', '16.g5', '-4e3', '-6.3e-4']
    >>> str2float(value_list)
    [5.3, -50000.0, 6.8, 3e+16, 19.1, 16.5, -4000.0, -0.00063]
    """
    if isinstance(value, (float, list, tuple, set)):
        # Original type.
        obj_type = type(value)
        return obj_type(map(str2float, value))
    elif not isinstance(value, str):
        raise TypeError(
            'Invalid inputs. Expected an argument of type str, '
            'tuple, list or set; got "%s" instead.' %
            value.__class__.__name__
        )

    try:
        return float(value)
    except ValueError:
        # Handled outside the block.
        pass

    accepted_chars = '.-e'
    lower_val = value.lower()

    # Filters out numeric values and those defined in `accepted_chars`.
    filtered_val = filter(
        lambda val: str.isnumeric(val) or val in accepted_chars and
        lower_val.count('-') <= 1 and
        not (lower_val.find('e') < lower_val.find('-') if 'e' in lower_val else False),
        lower_val
    )

    try:
        return float(str.join('', filtered_val))
    except ValueError as err:
        raise ValueError('%sValue does not match a numeric pattern supported in Python.' % err)


def str2int(value):
    """
    Converts numeric values from `str` or an array thereof to `int`.

    If numeric value is in the correct format, but contains invalid
    characters entered by mistake, such mistakes are automatically discarded.
    _Note_: Existence of `E` or `e` in the number is regarded as exponent, not
    a mistake.

    :param value: `str` or an array thereof containing numeric values.
    :type value: str, list, tuple, set
    :return: `int`, or an array of `int` numbers in the same type as the one given.
    :rtype: int, list, tuple, set

    >>> value = '3.4'
    >>> str2int(value)
    3

    >>> value = '3.4cvb'
    >>> str2int(value)
    3

    >>> value_list = {'3.4', '5.6'}
    >>> str2int(value_list)
    {3, 5}

    Timing for this example: 10000 loops, best of 3: 25.6 µs per loop
    >>> value_list = ['5.3fs', '-5e4', '6.8', '3e16', '19.1rgf', '16.g5', '-4e3', '-6.3e-4']
    >>> str2int(value_list)
    [5, -50000, 6, 30000000000000000, 19, 16, -4000, 0]
    """
    floated = str2float(value)

    # Original type.
    obj_type = type(value)

    if not isinstance(floated, float):
        # If not a single number:
        converted = map(int, floated)
    else:
        return int(floated)

    return obj_type(converted)


if __name__ == '__main__':
    from doctest import testmod
    # If ran directly, initiate doctests.
    testmod()
