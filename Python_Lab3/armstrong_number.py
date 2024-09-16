def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == num

print("Armstrong numbers between 1 and 1000 are:")
for number in range(1, 1001):
    if is_armstrong_number(number):
        print(number)
        
