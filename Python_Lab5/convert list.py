def convert_to_strings(int_list, int_tuple):
    # Convert the list of integers to a list of strings
    string_list = list(map(str, int_list))

    # Convert the tuple of integers to a list of strings
    string_tuple = list(map(str, int_tuple))

    return string_list, string_tuple

# Example usage:
int_list = [1, 2, 3, 4, 5]
int_tuple = (6, 7, 8, 9, 10)
string_list, string_tuple = convert_to_strings(int_list, int_tuple)
print("List of strings:", string_list)
print("Tuple of strings:", string_tuple)