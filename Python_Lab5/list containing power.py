def power_list(base, exponent_list):
    return list(map(lambda x: base ** x, exponent_list))

# Example usage:
base = 2
exponent_list = [0, 1, 2, 3, 4]
result = power_list(base, exponent_list)
print(result)  # Output: [1, 2, 4, 8, 16]