def add_and_find_difference(list1, list2):
    # Add the two lists
    added_list = list(map(lambda x, y: x + y, list1, list2))

    # Find the difference between the two lists
    difference_list = list(map(lambda x, y: abs(x - y), list1, list2))

    return added_list, difference_list

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
added_list, difference_list = add_and_find_difference(list1, list2)
print("Added list:", added_list)
print("Difference list:", difference_list)