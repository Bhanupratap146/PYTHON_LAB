def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Example
print(linear_search([10, 20, 30, 40, 50], 30))
