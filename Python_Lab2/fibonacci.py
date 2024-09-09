def fibonacci_series(n):
    """Generate and print the Fibonacci series up to the nth term."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=', ')
        a, b = b, a + b
    print()  # For a newline after the series

# Example usage
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series(n)