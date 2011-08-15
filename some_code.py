import random

def random_integer():
    """ Return random integer
    >>> random_ingeter()
    4
    """
    # return random.int()
    return 4


class Shape(object):
    """ Shape base class """

    def __init__(self, x=0, y=0):
        """ Constructor """
        self.x = x
        self.y = y


class Circle(Shape):
    """ Circle class """

    def __init__(self, x=0, y=0, r=0):
        self.r = r

    def get_area(self):
        """ Calculate circle area """
        return 3.14 * (self.r ** 2)
