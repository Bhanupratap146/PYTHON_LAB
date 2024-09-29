for i in range(8):
    # Print leading zeros
    print('0', end=' ')
    
    # Print table numbers
    for j in range(i):
        print(j * (i - 1), end=' ')
    
    # Print a newline
    print()