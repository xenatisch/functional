#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python:
from collections import defaultdict
from re import sub

# 3rd party:

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '04/05/2016, 01:00'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Analyser(object):
    def __init__(self, text=None, file_path=None):
        if text:
            self.text = self._prep(text)
        elif file_path:
            self.text = self._from_file(file_path)
        else:
            raise ValueError('Either a `_text` or `file_path` must be supplied.')

    def _prep(self, text):
        """
        Prepares the text by removing punctuation marks and splitting it into a list.
        :param text: Text to prepared.
        :type text: str
        :return: Prepared text.
        :rtype: list
        """
        # Removing punctuation marks.
        stripped = sub(r'[^\w\s]', '', str(text))

        # Splitting the string into a list (based on spaces).
        split = stripped.split()

        return split

    def analyse(self):
        """
        :return: A dictionary of words and their frequencies.
        :rtype: dict

        >>> my_text = "This is a nice, compact text. But it is short."
        >>> analyse_text = Analyser(text=my_text)
        """
        # Counting the recurrences.
        appr = defaultdict(int)
        for curr in self.text:
            appr[curr] += 1

        return appr

    def _from_file(self, file_path):
        """
        :param file_path:
        :type file_path:
        :return:
        :rtype:

        >>> test = Analyser(file_path='./test.txt')
        """
        try:
            with open(file_path, 'r') as file:
                tmp = [line for line in file]
                text = self._prep(tmp)

            return text

        except IOError as e:
            print('An error occurred whilst try to open the requested file.\n{err}'.format(err=e))
            return None

    def __str__(self):
        dict_obj = dict(self.analyse())
        string = reversed(sorted(dict_obj.items(), key=lambda x: x[1]))

        return str.join(
            '-'*30,
            list('\n   {:15}  |  {:5}\n  '.format(item, value) for item, value in string)
        )


class AnalyseWords(Analyser):
    def __init__(self, char, text=None, file_path=None):
        super().__init__(text, file_path)
        self._words_list = self._starts_with(char)

    def _starts_with(self, char):
        import re
        pattern = re.compile(r"\b[.{}]\w+".format(char))
        return pattern.findall(str.join(' ', self.text))

    def __str__(self):
        return '| ' + str.join(' | ', self._words_list) + ' |'


if __name__ == '__main__':
    import doctest
    test_res = doctest.testmod()

