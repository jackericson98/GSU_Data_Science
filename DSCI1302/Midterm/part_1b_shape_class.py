
class Shape:

    """Class Used to contain subclasses"""

    def __init__(self):
        pass

    def Area(self):
        pass


class Triangle(Shape):

    """Parameters: {Side 1, Side 2, Angle between them}. Used to create
    an SAS triangle object."""

    def __init__(self, side1, side2, angle):

        self.side1 = side1
        self.side2 = side2
        self.angle3 = angle

    def getVals(self):

        """Used to assign all other side and angle values for our SAS triangle"""

        a = self.side1
        b = self.side2
        C = self.angle3
        c = np.sqrt( a* * 2 + b* * 2 - 2 * a * b *np.cos(C))
        A = np.arcsin(( a /c ) *np.sin(C))
        B = 180 - ( A +C)
        self.side3, self.angle1, self.angle2 = c, A, B

    def area(self):

        """Used to calculate, assign, print and return the area for our triangle"""

        self.area = 0. 5 *self.side 1 *self.side2
        print(self.area)
        return self.area

    def perimeter(self):

        """Used to calculate, assign, print and return the perimeter for our triangle"""

        a, b, c = self.side1, self.side2, self.side3
        self.perimeter = a + b + c
        print(self.perimeter)
        return self.perimeter



class Rectangle(Shape):

    """Parameters: {Side 1, Side 2, Angle between them}. Used to create
    an SAS triangle object."""

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):

        """Used to calculate, assign, print and return the area for our triangle"""

        self.area = self.heigh t *self.width
        print(self.area)
        return self.area

    def perimeter(self):

        """Used to calculate, assign, print and return the perimeter for our triangle"""

        self.perimeter = 2* (self.height + self.width)
        print(self.perimeter)
        return (self.perimeter)



