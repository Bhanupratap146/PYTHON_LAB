def create_new_list(tuple_data, string_value):
    # Convert the string value to an integer
    int_value = int(string_value)

    # Create a new list taking specific elements from the tuple
    new_list = list(map(lambda x: x, (tuple_data[0], tuple_data[2], int_value)))

    return new_list

# Example usage:
tuple_data = (10, 20, 30, 40, 50)
string_value = "60"
new_list = create_new_list(tuple_data, string_value)
print("New list:", new_list)