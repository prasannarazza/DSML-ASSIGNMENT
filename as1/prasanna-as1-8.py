maths_marks = float(input("Enter marks in Mathematics: "))
physics_marks = float(input("Enter marks in Physics: "))
chemistry_marks = float(input("Enter marks in Chemistry: "))
total_marks = maths_marks + physics_marks + chemistry_marks
if maths_marks >= 60 and physics_marks >= 50 and chemistry_marks >= 40 and total_marks >= 200 and (maths_marks + physics_marks) >= 150:
    print("Eligible for admission")
else:
    print("Not eligible for admission")