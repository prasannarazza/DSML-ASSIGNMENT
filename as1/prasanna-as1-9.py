gross_salary = float(input("Enter gross salary: "))

if gross_salary < 10000:
    tax = 0
elif gross_salary < 20000:
    tax = 0.10 * gross_salary
elif gross_salary < 40000:
    tax = 0.15 * gross_salary
else:
    tax = 0.20 * gross_salary

net_salary = gross_salary - tax
print("Net Salary after tax deduction:", net_salary)