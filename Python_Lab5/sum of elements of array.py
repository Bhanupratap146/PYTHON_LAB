def sum_array_elements(array):
    # Use map to apply a lambda function to each element of the array
    # The lambda function simply returns the element itself
    mapped_array = list(map(lambda x: x, array))

    # Use the built-in sum function to compute the sum of the elements
    total_sum = sum(mapped_array)

    return total_sum

# Example usage:
array = [1, 2, 3, 4, 5]
total_sum = sum_array_elements(array)
print("Sum of array elements:", total_sum)