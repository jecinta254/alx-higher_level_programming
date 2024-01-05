#!/usr/bin/python3
"""This class define rectangle class"""


class Rectangle:
    """This rep a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Init new object of rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns: Area of our rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns: perimeter of our rectangle object
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns: # rep my rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            shape = []
            for i in range(self.__height):
                [shape.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    shape.append('\n')

            return ''.join(shape)

    def __repr__(self):
        """
        Returns: str rep of my rectangle
        """
        return f'Rectangle({str(self.__width)}, {str(self.__height)})'
