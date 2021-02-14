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


# Testing
if __name__ == '__main__':
    print(f"fibonacci(1) = {fibonacci(1)}")
    print(f"fibonacci(2) = {fibonacci(2)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(20) = {fibonacci(20)}")
    print(f"fibonacci(30) = {fibonacci(30)}")
    print(f"fibonacci(40) = {fibonacci(40)}")
