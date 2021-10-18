from typing import NamedTuple
import abc
import math


class Point2D(NamedTuple):
    """
    A point in 2-dimensional space.
    Implemented as NamedTuple (so it is immutable), but simple class can be used instead.
    """
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape2D(abc.ABC):
    """
    An abstract shape in 2-dimensional space. Examples of 2D shapes are rectangle, circle, etc.
    """
    @property
    @abc.abstractmethod
    def area(self) -> float:
        """Area of the shape."""
        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, point: Point2D) -> bool:
        """Check if the point is inside the shape.
        Support semantics like `if point in shape`"""
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        """Get string representation of the shape."""
        raise NotImplementedError


class Rectangle(Shape2D):
    def __init__(self, bottom_left: Point2D, width, length):
        self.bottom_left = bottom_left
        self.width = width
        self.length = length

    def __contains__(self, point):
        if self.bottom_left.x <= point.x <= self.bottom_left.x + self.width and self.bottom_left.y <= point.y <= self.bottom_left.y + self.length:
            return True
        else:
            return False

    def __str__(self):
        return f"Rectangle: bottom_left = [{self.bottom_left.x}, {self.bottom_left.y}], width = {self.width}, length = {self.length}"

    @property
    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, bottom_left: Point2D, width):
        super().__init__(bottom_left, width, width)

    def __str__(self):
        return f"Square: bottom_left = [{self.bottom_left.x}, {self.bottom_left.y}], side = {self.width}"


class Circle(Shape2D):
    def __init__(self, center: Point2D, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle: center = [{self.center.x}, {self.center.y}], radius = {self.radius}"

    def __contains__(self, point):
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 <= self.radius**2

    @property
    def area(self):
        return math.pi * self.radius**2


class Shape2DCollection(Shape2D):
    def __init__(self):
        self.shapes = []

    def __contains__(self, point):
        for shape in self.shapes:
            if point in shape:
                return True
        return False

    def __str__(self):
        shapes_str = '\n'.join(map(str, self.shapes))
        return f"Shape2DCollection:\n{shapes_str}"

    def add(self, shape):
        self.shapes.append(shape)

    @property
    def area(self):        
        return sum(map(lambda shape : shape.area, self.shapes))
