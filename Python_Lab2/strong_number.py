import math

num = int(input("Enter a number to check if it's a strong number: "))

digits = str(num)

sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)

if sum_of_factorials == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")