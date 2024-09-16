import math

def calculate_nCr(n, r):
    return math.comb(n, r)


try:
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    
    if r > n:
        print("r cannot be greater than n.")
    elif n < 0 or r < 0:
        print("n and r must be non-negative integers.")
    else:
        result = calculate_nCr(n, r)
        print(f"{n} choose {r} is: {result}")

except ValueError:
    print("Please enter valid integers.")

