from numpy.random import randint


class Quiz(object):
    def __init__(self, data):
        """
        :param data: A ``dict`` containing the data in the order shown in the example.
        :type data: dict
        """
        self.data = data
        self.total = len(self.data['questions'])
        self.iterator = 0


class RandomQuestion(Quiz):
    def _get_fields(self):
        data_dict = self.data

        # Separate questions
        questions_col = data_dict['questions']

        # Separate choices + correct answer.
        choices_col = data_dict['choices']

        return questions_col, choices_col

    def _get_item(self):
        questions_col, choices_col = self._get_fields()

        # Generator
        while len(questions_col) != 0:
            item_ind = randint(0, len(questions_col))
            question = questions_col.pop(item_ind)
            choices = choices_col.pop(item_ind)
            correct = choices.pop(-1)
            yield question[-1], choices, correct

    def __str__(self):
        """
        :return: A single, randomly selected item that includes "question, choices, and answer".
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

        >>> item = RandomQuestion(data)

        The contents will look as follows:

        .. code-block:: python
            Who was the inventor of Python?
            ['Silvester Stallone', 'Guido van Rossum', 'Neither']
            2
        """
        values = self._get_item().__next__()
        return str.join('\n', map(str, values))


class Outputs():
    pass

class MakeCSV(Outputs):
    pass


class CheckAnswer(Quiz):
    pass


class KeepScore(Quiz):
    pass


if __name__ == "__main__":
    import doctest
    test_res = doctest.testmod()
