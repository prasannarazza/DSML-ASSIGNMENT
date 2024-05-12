numbers = [float(input("Enter number {}: ".format(i+1))) for i in range(10)]
smallest = min(numbers)
largest = max(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
