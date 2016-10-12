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
from utils.QuizTools.quiz import RandomQuestion

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__author__ = 'Pouria Hadjibagheri'
__copyright__ = 'Copyright 2016'
__credits__ = ['Pouria Hadjibagheri']
__license__ = 'MIT'
__maintainer__ = 'Pouria Hadjibagheri'
__email__ = 'p.bagheri.12@ucl.ac.uk'
__date__ = '04/05/2016, 11:25'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class RandomQuiz(RandomQuestion):
    def get_question(self):
        """
        :return: A randomly selected ``list`` containing ``[question, choices, answer]`` if one exists,
                 otherwise ``None``.
        :rtype: list, None

        Example:
        --------------------------
        .. code-block:: python
            >>> data = {
            ...     'questions': [
            ...         ["What year was Charles Darwin born?"],
            ...         ["Who was the inventor of Python?"],
            ...         ["Who wrote the book entitled 'An then there were none'?"]
            ...     ]
            ...     ,
            ...     'choices': [
            ...         ["1945", "1766", "1809", 3],
            ...         ["Silvester Stallone", "Guido van Rossum", "Neither", 2],
            ...         ["Agata Christie", "Charles Dickens", 1]
            ...     ]
            ... }

        The last entry in ``choices``  must be an int, corresponding to the ``index`` of the correct choice in
        the ``list``.

        .. code-block:: python
            >>> qz = RandomQuiz(data)
            >>> while True:
            ...     items = qz.get_question()
            ...     if items:
            ...         randomised_quiz = "Question: {} | Choices: {} | Correct: {}".format(*items)
            ...         # Print or do additional operations.
            ...     else:
            ...         break

            Question: What year was Charles Darwin born? | Choices: ['1945', '1766', '1809'] | Correct: 3
            Question: Who wrote the book entitled 'An then there were none'? | Choices: ['Agata Christie',
            'Charles Dickens'] | Correct: 1
            Question: Who was the inventor of Python? | Choices: ['Silvester Stallone', 'Guido van Rossum',
            'Neither'] | Correct: 2

        """
        self.iterator += 1

        return self._get_item().__next__() if self.iterator <= self.total else None

    def randomised_list(self):
        """
        :return: A list of tuples, each of which contain (question, choices, answer).
        :rtype: list

        >>> data = {
        ...     'questions': [
        ...         ["What year was Charles Darwin born?"],
        ...         ["Who was the inventor of Python?"],
        ...         ["Who wrote the book entitled 'An then there were none'?"]
        ...     ]
        ...     ,
        ...     'choices': [
        ...         ["1945", "1766", "1809", 3],
        ...         ["Silvester Stallone", "Guido van Rossum", "Neither", 2],
        ...         ["Agata Christie", "Charles Dickens", 1]
        ...     ]
        ... }

        >>> qz = RandomQuiz(data)
        >>> rand_quiz = qz.randomised_list()

        The contents will look as follows:

        .. code-block:: python
            [
                ("Who wrote the book entitled 'An then there were none'?", ['Agata Christie', 'Charles Dickens'], 1),
                ('What year was Charles Darwin born?', ['1945', '1766', '1809'], 3),
                ('Who was the inventor of Python?', ['Silvester Stallone', 'Guido van Rossum', 'Neither'], 2)
            ]
        """
        return [(ques, choices, ans) for ques, choices, ans in self._get_item()]

    def randomised_dict(self):
        """
        :return: A dictionary containing 3 keys: Question, Choices, and Answers.
        :rtype: dict

        >>> data = {
        ...     'questions': [
        ...         ["What year was Charles Darwin born?"],
        ...         ["Who was the inventor of Python?"],
        ...         ["Who wrote the book entitled 'An then there were none'?"]
        ...     ]
        ...     ,
        ...     'choices': [
        ...         ["1945", "1766", "1809", 3],
        ...         ["Silvester Stallone", "Guido van Rossum", "Neither", 2],
        ...         ["Agata Christie", "Charles Dickens", 1]
        ...     ]
        ... }

        >>> qz = RandomQuiz(data)
        >>> rand_test = qz.randomised_dict()

        The contents will look as follows:

        .. code-block:: python
            {
                'question': (
                    'Who was the inventor of Python?',
                    'What year was Charles Darwin born?',
                    "Who wrote the book entitled 'An then there were none'?"
                ),
                'answers': (2, 3, 1),
                'choices': (
                    ['Silvester Stallone', 'Guido van Rossum', 'Neither'],
                    ['1945', '1766', '1809'],
                    ['Agata Christie', 'Charles Dickens']
                )
            }
        """
        keys = ['question', 'choices', 'answers']
        items = ((ques, choices, ans) for ques, choices, ans in self._get_item())

        return dict(zip(keys, zip(*items)))

    def __str__(self):
        """
        :return: The entire set of items as '(questions, choices and answers)'.
        :rtype: str

        >>> data = {
        ...     'questions': [
        ...         ["What year was Charles Darwin born?"],
        ...         ["Who was the inventor of Python?"],
        ...         ["Who wrote the book entitled 'An then there were none'?"]
        ...     ]
        ...     ,
        ...     'choices': [
        ...         ["1945", "1766", "1809", 3],
        ...         ["Silvester Stallone", "Guido van Rossum", "Neither", 2],
        ...         ["Agata Christie", "Charles Dickens", 1]
        ...     ]
        ... }

        The contents will look as follows:

        .. code-block:: python
            ("Who wrote the book entitled 'An then there were none'?", ['Agata Christie', 'Charles Dickens'], 1)
            ('What year was Charles Darwin born?', ['1945', '1766', '1809'], 3)
            ('Who was the inventor of Python?', ['Silvester Stallone', 'Guido van Rossum', 'Neither'], 2)
        """
        string_items = (str((ques, choices, ans)) for ques, choices, ans in self._get_item())
        return str.join('\n', string_items)


if __name__ == "__main__":
    import doctest
    test_res = doctest.testmod()
