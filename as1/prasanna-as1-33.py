class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.feet * 12 + self.inches + other.feet * 12 + other.inches
        new_feet, new_inches = divmod(total_inches, 12)
        return Distance(new_feet, new_inches)

# Example usage:
distance1 = Distance(5, 8)
distance2 = Distance(3, 10)

total_distance = distance1 + distance2
print("Total Distance:", total_distance.feet, "feet", total_distance.inches, "inches")
