# Take input from the user
user_input = input("Enter a string: ")

# Initialize a counter for vowels
vowel_count = 0

# Define the vowels
vowels = 'aeiouAEIOU'

# Iterate over each character in the string
for char in user_input:
    # Check if the character is a vowel
    if char in vowels:
        # Increment the vowel count
        vowel_count += 1

# Print the number of vowels
print("Number of vowels:", vowel_count)