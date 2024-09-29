for i in range(1, 6):
    # Print numbers in descending order
    for j in range(10, 0, -2):
        print(j, end=' ')
        if j <= 2 * (6 - i):
            break
    
    # Print a newline
    print()