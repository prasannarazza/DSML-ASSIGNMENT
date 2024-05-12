class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other_distance):
        total_inches = self.feet * 12 + self.inches + other_distance.feet * 12 + other_distance.inches
        new_feet, new_inches = divmod(total_inches, 12)
        return Distance(new_feet, new_inches)

    def compare(self, other_distance):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other_distance.feet * 12 + other_distance.inches
        if total_inches_self > total_inches_other:
            return "First distance is greater"
        elif total_inches_self < total_inches_other:
            return "Second distance is greater"
        else:
            return "Distances are equal"

# Example usage:
distance1 = Distance(5, 8)
distance2 = Distance(3, 10)

print("Sum of Distance 1 and Distance 2:", distance1.add(distance2).feet, "feet", distance1.add(distance2).inches, "inches")
print("Comparison of Distance 1 and Distance 2:", distance1.compare(distance2))
