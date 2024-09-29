for i in range(5, 0, -1):
    # Print leading spaces
    print(' ' * (5 - i), end='')
    
    # Print numbers
    for j in range(i):
        print(i, end=' ')
    
    # Print a newline
    print()