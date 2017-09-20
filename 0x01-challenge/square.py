#!/usr/bin/python3
"""
Defines Square class
"""


class Square():
    """ attributes and methods for Square objects """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes Square object """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ area of the square """
        return self.width * self.width

    def perimeter(self):
        """ perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
