def iterate_simultaneously(list1, list2):
    for item1, item2 in zip(list1, list2):
        print(item1, item2)

# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
iterate_simultaneously(list1, list2)
# Output:
# 1 a
# 2 b
# 3 c
