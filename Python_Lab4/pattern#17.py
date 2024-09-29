for i in range(6, 0, -1):
    # Print leading spaces
    print(' ' * (6 - i), end='')
    
    # Print stars
    for j in range(i):
        print('*', end=' ')
    
    # Print a newline
    print()