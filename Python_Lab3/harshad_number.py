def is_harshad_number(num):
    num_str = str(num)  
    digit_sum = sum(int(digit) for digit in num_str)  
    
    
    return digit_sum != 0 and num % digit_sum == 0


try:
    number = int(input("Enter a number to check if it is a Harshad number: "))
    if is_harshad_number(number):
        print(f"{number} is a Harshad number.")
    else:
        print(f"{number} is not a Harshad number.")
except ValueError:
    print("Please enter a valid integer.")
