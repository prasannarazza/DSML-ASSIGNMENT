numbers = [float(input("Enter number {}: ".format(i+1))) for i in range(10)]
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
print("Sum:", sum_numbers)
print("Average:", average)