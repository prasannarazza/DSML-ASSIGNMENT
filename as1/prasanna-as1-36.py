file_name = input("Enter the name of the text file: ")

with open(file_name, 'r') as file:
    text = file.read()

num_whitespace = sum(1 for char in text if char.isspace())

print("Number of whitespace characters:", num_whitespace)
