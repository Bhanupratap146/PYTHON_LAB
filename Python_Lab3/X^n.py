def compute_power(x, n):
    return x ** n


try:
    x = float(input("Enter the base (X): "))
    n = int(input("Enter the exponent (n): "))
    
    result = compute_power(x, n)
    print(f"{x} raised to the power of {n} is: {result}")

except ValueError:
    print("Please enter valid numbers. Base should be a number and exponent should be an integer.")
