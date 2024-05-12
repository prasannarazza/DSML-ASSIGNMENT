class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def circumference(self):
        return 2 * Circle.PI * self.radius

# Example usage:
circle1 = Circle(5)
print("Area of Circle 1:", circle1.area())
print("Circumference of Circle 1:", circle1.circumference())

circle2 = Circle(3)
print("Area of Circle 2:", circle2.area())
print("Circumference of Circle 2:", circle2.circumference())
