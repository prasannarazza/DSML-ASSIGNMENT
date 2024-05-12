file_name = input("Enter the name of the text file: ")

with open(file_name, 'r') as file:
    text = file.read()

num_characters = len(text)
num_vowels = sum(1 for char in text if char.lower() in 'aeiou')
num_consonants = sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')
num_words = len(text.split())
num_lines = text.count('\n') + 1

print("Number of characters:", num_characters)
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
