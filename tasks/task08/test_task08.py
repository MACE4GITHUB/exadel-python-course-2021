import unittest
from task08 import Point2D, Rectangle, Square, Circle, Shape2DCollection


class TestTask08(unittest.TestCase):
    def getPoint2D(self):
        return Point2D(1, 2)

    def test_rectangle_includes_point2D(self):
        point2D = Point2D(4, 9)
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        self.assertIn(point2D, rectangle)

    def test_rectangle_not_includes_point2D(self):
        point2D = Point2D(40, 90)
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        self.assertFalse(point2D in rectangle)

    def test_rectangle_area(self):
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        self.assertEqual(rectangle.area, 27)

    def test_square_includes_point2D(self):
        square = Square(self.getPoint2D(), 8)
        self.assertIn(self.getPoint2D(), square)

    def test_square_not_includes_point2D(self):
        point2D = Point2D(1, 1)
        square = Square(self.getPoint2D(), 7)
        self.assertFalse(point2D in square)

    def test_square_area(self):
        square = Square(self.getPoint2D(), 21)
        self.assertEqual(square.area, 441)

    def test_circle_includes_point2D(self):
        square = Square(self.getPoint2D(), 17)
        self.assertIn(self.getPoint2D(), square)

    def test_circle_not_includes_point2D(self):
        point2D = Point2D(6, 90)
        square = Square(self.getPoint2D(), 72)
        self.assertFalse(point2D in square)

    def test_square_circle(self):
        circle = Circle(self.getPoint2D(), 34)
        self.assertEqual(circle.area, 3631.681107549801)

    def test_point_in_shape2DCollection(self):
        point2D = Point2D(5, 8)
        circle = Circle(self.getPoint2D(), 40)
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        square = Square(self.getPoint2D(), 30)
        shape2DCollection = Shape2DCollection()
        shape2DCollection.add(circle)
        shape2DCollection.add(rectangle)
        shape2DCollection.add(square)
        self.assertIn(point2D, shape2DCollection)

    def test_point_not_in_shape2DCollection(self):
        point2D = Point2D(31, 65)
        circle = Circle(self.getPoint2D(), 42)
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        square = Square(self.getPoint2D(), 30)
        shape2DCollection = Shape2DCollection()
        shape2DCollection.add(circle)
        shape2DCollection.add(rectangle)
        shape2DCollection.add(square)
        self.assertFalse(point2D in shape2DCollection)

    def test_square_shape2DCollection(self):
        circle = Circle(self.getPoint2D(), 62)
        rectangle = Rectangle(self.getPoint2D(), 3, 9)
        square = Square(self.getPoint2D(), 7)
        shape2DCollection = Shape2DCollection()
        shape2DCollection.add(circle)
        shape2DCollection.add(rectangle)
        shape2DCollection.add(square)
        self.assertEqual(shape2DCollection.area, 12152.282160399165)


if __name__ == '__main__':
    unittest.main()
