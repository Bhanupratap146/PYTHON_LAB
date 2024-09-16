def is_disarium_number(num):
    num_str = str(num)  
    total = 0
    
    
    for i, digit in enumerate(num_str):
        total += int(digit) ** (i + 1)
    
    return total == num

try:
    number = int(input("Enter a number to check if it is a Disarium number: "))
    if is_disarium_number(number):
        print(f"{number} is a Disarium number.")
    else:
        print(f"{number} is not a Disarium number.")
except ValueError:
    print("Please enter a valid integer.")

