def add_after_item(lst, item_to_insert_after, new_item):
    index = lst.index(item_to_insert_after)
    lst.insert(index + 1, new_item)
    return lst

# Example usage:
my_list = ['apple', 'banana', 'orange']
modified_list = add_after_item(my_list, 'banana', 'grape')
print(modified_list)  # Output: ['apple', 'banana', 'grape', 'orange']
