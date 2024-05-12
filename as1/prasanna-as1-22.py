numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(10)]
sum_even = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", sum_even)
