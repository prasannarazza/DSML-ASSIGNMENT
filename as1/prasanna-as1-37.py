input_file_name = input("Enter the name of the input text file: ")
output_file_name = input("Enter the name of the output text file: ")

with open(input_file_name, 'r') as input_file:
    numbers = [float(num) for num in input_file.read().split()]

total_sum = sum(numbers)
average = total_sum / len(numbers)

with open(output_file_name, 'w') as output_file:
    output_file.write("Sum of numbers: {}\n".format(total_sum))
    output_file.write("Average of numbers: {:.2f}\n".format(average))
