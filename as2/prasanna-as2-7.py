def extend_nested_list(nested_list, sublist):
    nested_list.extend(sublist)
    return nested_list

# Example usage:
nested_list = [[1, 2], [3, 4]]
sublist = [5, 6]
extended_list = extend_nested_list(nested_list, sublist)
print(extended_list)  # Output: [[1, 2], [3, 4], 5, 6]
