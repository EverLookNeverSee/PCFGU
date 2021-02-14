""" Recursive implementation of fibonacci numbers with exponential growth """


def fibonacci(n: int) -> int:
    """
    Recursive implementation
    :param n: nth number of series that we want to calculate
    :return: nth number of series
    """
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
