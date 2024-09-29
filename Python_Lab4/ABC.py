# Task A: Separate the string into comma-separated values
X = "India.is.my.country"
X_values = X.replace('.', ',')
print("Comma-separated values:", X_values)

# Task B: Remove a given character from a string
Y = "M.A.N.I.P.A.L"
char_to_remove = 'A'
Y_removed = Y.replace(char_to_remove, '')
print("String after removing", char_to_remove, ":", Y_removed)

# Task C: Remove the dots from the string
Y_dots_removed = Y.replace('.', '')
print("String after removing dots:", Y_dots_removed)