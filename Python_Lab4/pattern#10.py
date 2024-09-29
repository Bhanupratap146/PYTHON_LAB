for i in range(1, 6):
    # Print numbers in ascending order
    for j in range(1, i + 1):
        print(j, end=' ')
    
    # Print numbers in descending order
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    
    # Print a newline
    print()