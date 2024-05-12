class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Example usage:
rect1 = Rectangle(4, 5)
print("Area of Rectangle 1:", rect1.area())
print("Perimeter of Rectangle 1:", rect1.perimeter())

rect2 = Rectangle(3, 6)
print("Area of Rectangle 2:", rect2.area())
print("Perimeter of Rectangle 2:", rect2.perimeter())
