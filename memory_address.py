def find_first_repeating_character(s):
    # Dictionary to keep track of character counts
    char_count = {}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, it's the first repeating character
        if char in char_count:
            # Print the character and its memory address
            memory_address = id(char)
            print(f"The first repeating character is '{char}' with memory address {memory_address}")
            return char, memory_address
        else:
            # If the character is not in the dictionary, add it
            char_count[char] = 1
    
    # If no repeating character is found, return None
    print("No repeating character found")
    return None

# Example usage
result = find_first_repeating_character("sample phrase")
print(result)  # Should print the first repeating character and its memory address

