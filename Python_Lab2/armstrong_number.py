# Input the number to check
number = int(input("Enter a number to check if it's an Armstrong number: "))

# Convert the number to string to iterate over digits
digits = str(number)
num_digits = len(digits)

# Calculate the sum of each digit raised to the power of num_digits
sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

# Check if the sum of powers equals the original number
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")