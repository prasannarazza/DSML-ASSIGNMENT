number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

if armstrong_sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
