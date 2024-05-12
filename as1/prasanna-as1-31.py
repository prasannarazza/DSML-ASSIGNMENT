class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def division(self):
        percentage = self.percentage()
        if percentage >= 60:
            return "First Division"
        elif percentage >= 45:
            return "Second Division"
        elif percentage >= 33:
            return "Third Division"
        else:
            return "Fail"

# Example usage:
student1 = Student("John", "A001", [80, 75, 85, 90, 88])
student2 = Student("Alice", "A002", [65, 70, 75, 80, 82])

print("Total marks obtained by", student1.name, ":", student1.total())
print("Percentage obtained by", student1.name, ":", student1.percentage())
print("Division obtained by", student1.name, ":", student1.division())

print("Total marks obtained by", student2.name, ":", student2.total())
print("Percentage obtained by", student2.name, ":", student2.percentage())
print("Division obtained by", student2.name, ":", student2.division())
