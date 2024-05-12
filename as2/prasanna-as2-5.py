def remove_empty_strings(lst):
    return [item for item in lst if item != '']

# Example usage:
my_list = ['hello', '', 'world', '', '']
filtered_list = remove_empty_strings(my_list)
print(filtered_list)  # Output: ['hello', 'world']
