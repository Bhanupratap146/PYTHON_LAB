def sum_of_digits(num):
    
    num_str = str(abs(num))
    
    
    digit_sum = sum(int(digit) for digit in num_str)
    
    return digit_sum


try:
    number = int(input("Enter a number to find the sum of its digits: "))
    result = sum_of_digits(number)
    print(f"The sum of the digits in {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
