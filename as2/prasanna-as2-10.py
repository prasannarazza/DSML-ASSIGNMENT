def transpose_nested_list(nested_list):
    return [list(row) for row in zip(*nested_list)]

# Example usage:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_list = transpose_nested_list(nested_list)
print(transposed_list)
# Output:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
