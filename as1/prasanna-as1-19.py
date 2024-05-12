numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(10)]
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
