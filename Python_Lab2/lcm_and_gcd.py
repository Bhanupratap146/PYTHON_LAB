import math

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
gcd = math.gcd(num1, num2)

# Calculate LCM using the formula
lcm = abs(num1 * num2) // gcd

# Display the results
print(f"The GCD of {num1} and {num2} is: {gcd}")
print(f"The LCM of {num1} and {num2} is: {lcm}")