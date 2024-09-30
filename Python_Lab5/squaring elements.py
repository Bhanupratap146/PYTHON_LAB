def square_elements(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]