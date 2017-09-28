#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle():
    """ attributes and methods for Rectangle objects """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes Rectangle object """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ perimeter of the rectangle """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the rectangle """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    r = Rectangle(width=12, height=9)
    print(r)
    print(r.area())
    print(r.perimeter())
