def replace_item(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
modified_list = replace_item(my_list, 3, 10)
print(modified_list)  # Output: [1, 2, 10, 4, 5]
