class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.height * self.depth + self.width * self.depth)

# Example usage:
box1 = Box(3, 4, 5)
print("Volume of Box 1:", box1.volume())
print("Surface Area of Box 1:", box1.surface_area())

box2 = Box(2, 3, 6)
print("Volume of Box 2:", box2.volume())
print("Surface Area of Box 2:", box2.surface_area())
