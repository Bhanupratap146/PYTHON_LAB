for i in range(1, 6):
    # Print leading spaces
    print(' ' * (5 - i), end='')
    
    # Print numbers
    for j in range(1, i + 1):
        print(j, end=' ')
    
    # Print a newline
    print()