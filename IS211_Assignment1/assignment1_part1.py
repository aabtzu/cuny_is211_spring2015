__author__ = 'amit'


def listDivide(numbers, divide=2):

    """
    The function returns the number of elements in the numbers list that are divisible by divide.
    """

    n = 0
    for nn in numbers:
        if nn % divide == 0:
            n += 1
    return n


class ListDivideException(Exception):
    pass


def testListDivide():
    try:
        assert(listDivide([1, 2, 3, 4, 5]) == 2)   # should return 2
        assert(listDivide([2, 4, 6, 8, 10]) == 5)   # should return 5
        assert(listDivide([30, 54, 63, 98, 100], divide=10) == 2)  # should return 2
        assert(listDivide([]) == 0)   # should return 0
        assert(listDivide([1, 2, 3, 4, 5], 1) == 5)   # should return 5
    except:
        raise ListDivideException()


if __name__ == "__main__":
    testListDivide()
