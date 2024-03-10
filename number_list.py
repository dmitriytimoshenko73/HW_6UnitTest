"""Модуль содержит класс NumberList"""


class NumberList:
    """Класс для нахождения среднего значения двух списков."""
    @staticmethod
    def get_average(number_list: list) -> float:
        """Возвращает среднее значение списка.

        Parameters:
            number_list: list (список)

        Returns:
            float: average value of list (среднее значение списка)
        """
        if not isinstance(number_list, list):
            raise TypeError('There should be a list of numbers!')
        for element in number_list:
            if not isinstance(element, float | int):
                raise ValueError('There should be a numbers in list.')
        if not number_list:
            return 0
        return sum(number_list) / len(number_list)

    @staticmethod
    def compare_values(average_1: float, average_2: float) -> str:
        """Сравнение двух средних значений.

        Parameters:
            average_1: float
            average_2: float

        Returns:
            str: the result of comparing two values (результат сравнения двух значений)
        """
        if average_1 > average_2:
            return 'The first list has a larger average value.'
        if average_2 > average_1:
            return 'The second list has a larger average value.'
        return 'The average values are equal.'