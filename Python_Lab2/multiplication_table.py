def print_multiplication_table(number, range_limit):
    """Print the multiplication table for a given number up to a specified range."""
    print(f"Multiplication Table for {number}")
    for i in range(1, range_limit + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
number = int(input("Enter the number for which you want to print the multiplication table: "))
range_limit = int(input("Enter the range limit for the multiplication table: "))
print_multiplication_table(number, range_limit)