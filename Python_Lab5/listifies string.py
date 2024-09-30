def listify_strings(strings):
    return list(map(list, strings))

# Example usage:
strings = ["hello", "world", "python"]
listified_strings = listify_strings(strings)
print(listified_strings)  # Output: [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd'], ['p', 'y', 't', 'h', 'o', 'n']]