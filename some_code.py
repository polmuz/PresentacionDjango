# -*- coding: utf-8 -*-

import random


def random_integer():
    """ Return random integer
    >>> random_integer()
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
    """ Circle """

    def __init__(self, x=0, y=0, r=0):
        self.r = r
        super(Circle, self).__init__(x, y)

    def get_area(self):
        """ Calculate circle area """
        return 3.14 * (r ** 2)



