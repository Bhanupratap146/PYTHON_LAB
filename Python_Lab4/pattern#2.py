for i in range(1, 6):
    # Print leading spaces
    print(' ' * (i - 1), end='')
    
    # Print numbers
    for j in range(6 - i):
        print(i, end=' ')
    
    # Print a newline
    print()