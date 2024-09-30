def fibonacci_squares(n):
    # Generate the first N Fibonacci numbers
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    # Compute the square of each Fibonacci number using map
    squared_numbers = list(map(lambda x: x ** 2, fibonacci_numbers))

    return squared_numbers

# Example usage:
n = 10
squared_numbers = fibonacci_squares(n)
print("Squared Fibonacci numbers:", squared_numbers)