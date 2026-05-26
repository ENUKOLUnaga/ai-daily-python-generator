def reverse_string(input_str):
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Use slicing to reverse the string
    reversed_str = input_str[::-1]
    
    # Return the reversed string
    return reversed_str

# Test the function
input_str = "Hello World"
print("Original String: ", input_str)
print("Reversed String: ", reverse_string(input_str))