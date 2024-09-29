def print_connected_inverted_pyramid(n):
    
    # Loop through each row
    for row in range(1, n + 1):
        # Print decreasing numbers
        for i in range(n, row - 1, -1):
            print(i, end=" ")
        # Print increasing numbers
        for i in range(row , n + 1):
            print(i, end=" ")
        print()

# Test the function
print_connected_inverted_pyramid(5)
