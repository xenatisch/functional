#!/usr/bin/env python3

"""
<Description of the programme>

Programmed in Python 3.5.1-final.
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Python:

# 3rd party:

# Internal:
from TextTools.Analyses import Analyser

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '03/05/2016, 20:45'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class _ResultFactory(Analyser):
    def _results(self, threshold, display=True):
        """
        :param threshold:
        :type threshold:
        :param display:
        :type display:
        :return:
        :rtype:
        """
        appearances = self.analyse()
        joined_args = str.join(
            "\n",
            (val for val in appearances if appearances[val] > threshold)
        )
        response = "Words appearing more than {} times:\n".format(threshold) + joined_args

        return response if not display else print(response)


class _GraphicsFactory(Analyser):
    def _plotit(self, display=False):
        """
        :return: Figure object of the graph for the analysis produced by Matplotlib.
        :rtype: matplotlib.pyplot.figure
        """
        appearances = self.analyse()
        from matplotlib.pyplot import (
            figure, bar, xticks, xlim, grid,
            show, style
        )
        try:
            style.use('ggplot')
        except Exception as e:
            pass

        # Separate the data
        total_items = range(len(appearances))
        frequencies = list(appearances.values())
        words = list(appearances.keys())

        # Plot
        fig = figure(figsize=[16, 9])
        bar(total_items, frequencies)
        xticks(total_items, words, rotation='vertical')
        xlim(min(total_items), max(total_items) + 1)
        grid('off')

        return fig if not display else show()


class AnalyseText(_ResultFactory, _GraphicsFactory):
    def report(self, threshold, display=True):
        """
        :param threshold:
        :type threshold:
        :param display:
        :type display:
        :return:
        :rtype:

        .. code-block:: python
            >>> my_text = "This is a nice, compact text. But it is short."
            >>> test = AnalyseText(text=my_text)
            >>> test.report(threshold=1, display=True)
            Words appearing more than 1 times:
            is
        """
        return self._results(threshold=threshold, display=display)

    def plot_results(self, display=False):
        """
        :return: Figure object of the graph for the analysis produced by Matplotlib.
        :rtype: matplotlib.pyplot.figure

        .. code-block:: python
            >>> my_text = "This is a nice, compact text. But it is short."
            >>> fig = AnalyseText(text=my_text).plot_results()
            >>> fig.show()
        """
        return self._plotit(display=display)


if __name__ == '__main__':
    import doctest
    test_res = doctest.testmod()
