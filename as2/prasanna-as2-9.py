def remove_all_occurrences(lst, item_to_remove):
    return [item for item in lst if item != item_to_remove]

# Example usage:
my_list = [1, 2, 3, 2, 4, 2, 5]
modified_list = remove_all_occurrences(my_list, 2)
print(modified_list)  # Output: [1, 3, 4, 5]
