def convert_and_eliminate_duplicates(sequence):
    # Convert to uppercase and lowercase
    uppercase_sequence = list(map(lambda x: x.upper(), sequence))
    lowercase_sequence = list(map(lambda x: x.lower(), sequence))

    # Eliminate duplicates
    unique_uppercase_sequence = list(set(uppercase_sequence))
    unique_lowercase_sequence = list(set(lowercase_sequence))

    return unique_uppercase_sequence, unique_lowercase_sequence

# Example usage:
sequence = "Hello World"
uppercase_sequence, lowercase_sequence = convert_and_eliminate_duplicates(sequence)
print("Uppercase sequence:", uppercase_sequence)
print("Lowercase sequence:", lowercase_sequence)