def add_three_lists(list1, list2, list3):
    return list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# Example usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = add_three_lists(list1, list2, list3)
print(result)  # Output: [12, 15, 18]