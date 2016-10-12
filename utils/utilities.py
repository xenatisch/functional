#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '30/04/2016, 12:24'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def irange(stop, start=0, step=1):
    """
    Returns an inclusive range generator.
    :param stop: Last number.
    :type stop: int, float
    :param start: First number.
    :type start: int, float
    :param step: Incrementing / decrementing step.
    :type step: int, float
    :return: Generator of a range from start to end incremented / decremented by step.
    :rtype: generator

    Examples:
    --------------------------
    Create a generator object.
    .. code-block:: python
        >>> my_range = irange(5, 0, .5)
        >>> print(type(my_range))
        <class 'generator'>

    Retrieve a list containing actual items.
    .. code-block:: python
        >>> print(list(my_range))
        [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    Manipulate the items and store them in a list.
    .. code-block:: python
        >>> print([val**2 for val in irange(2, 0, .5)])
        [0, 0.25, 1.0, 2.25, 4.0]

    Use ``map`` to manipulate the items without creating a list.
    .. code-block:: python
        >>> rng = map(lambda x: x-2, irange(2, 0, .5))
        >>> print(list(rng))
        [-2, -1.5, -1.0, -0.5, 0.0]
    """
    numerator = start
    while numerator <= stop:
        yield numerator
        numerator += step


def find_unique(a, b):
    """
    :param a: Iterable number 1.
    :type a: list, tuple
    :param b: Iterable number 2.
    :type b: list, tuple
    :return: List of unique objects from both ``a`` and ``b``.
    :rtype: list

    Example:
    --------------------------
    .. code-block:: python
        >>> list_1 = [1, 2, 3]
        >>> list_2 = [1, 5, 2]
        >>> unique_items = find_unique(list_1, list_2)
        >>> print(unique_items)
        [3, 5]
        >>> type(unique_items)
        <class 'list'>
    """
    set_a = set(a)
    set_b = set(b)
    unique = set_a - set_b
    unique |= set_b - set_a
    return list(unique)


def is_even(val):
    """
    Confirms if a value if even.
    :param val: Value to be tested.
    :type val: int, float
    :return: True if the number is even, otherwise false.
    :rtype: bool

    Examples:
    --------------------------
    .. code-block:: python
        >>> even_numbers = list(filter(is_even, range(20)))
        >>> print(even_numbers)
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

        >>> print(is_even(9))
        False

        >>> print(is_even(-2))
        True

        >>> print([value for value in range(20) if is_even(value)])
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

        >>> print([is_even(value) for value in range(4)])
        [True, False, True, False]
    """
    return (val % 2) == 0


def is_odd(val):
    """
    Confirms if a value if odd.
    :param val: Value to be tested.
    :type val: int, float
    :return: True if the number is odd, otherwise false.
    :rtype: bool

    Examples:
    --------------------------
    .. code-block:: python
        >>> even_numbers = list(filter(is_odd, range(20)))
        >>> print(even_numbers)
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        >>> print(is_odd(10))
        False

        >>> print(is_odd(-3))
        True

        >>> print([value for value in range(20) if is_odd(value)])
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        >>> print([is_odd(value) for value in range(4)])
        [False, True, False, True]
    """
    return (val % 2) != 0


class HexRgb:
    @staticmethod
    def int2rgb(rgbint):
        """
        Converts integer colour values of 6 digits long (575757) to RGB values (8, 201, 13).

        Example:
        --------------------------
        .. code-block:: python
            >>> HexRgb.int2rgb(575757)
            (8, 201, 13)
        """
        # Check the integrity of the input.
        if not(isinstance(rgbint, int) and 0 <= rgbint <= 16777215):
            error_msg = (
                "\nInput to the function must be a 1 to 8 digit long integer, "
                "between 0 and 16777215. Got <{va}> of {ty} instead.".format(
                    va=rgbint,
                    ty=type(rgbint)
                )
            )

            raise ValueError(error_msg)

        # Calculating the RGB values.
        red = rgbint // 256 // 256 % 256
        green = rgbint // 256 % 256
        blue = rgbint % 256

        return red, green, blue

    @staticmethod
    def rgb2hex(red, green, blue):
        """
        Converts RGB values (8, 201, 13) to Hex (#08c90d).

        Example:
        --------------------------
        .. code-block:: python
            >>> HexRgb.rgb2hex(8, 201, 13)
            '#08c90d'
        """
        args = [red, green, blue]
        for val in args:
            if not(isinstance(val, int) and 0 <= val <= 255):
                error_msg = (
                    "\nInput to the function must be 3 separate integers, "
                    "each of which between 0 and 255. Got <{va}> with a length of "
                    "{ty} instead.".format(
                        va=val,
                        ty=type(val)
                    )
                )
                raise ValueError(error_msg)

        return '#%02x%02x%02x' % (red, green, blue)


if __name__ == "__main__":
    import doctest
    test_res = doctest.testmod()

