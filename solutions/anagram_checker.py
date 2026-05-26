def are_anagrams(str1, str2):
    # Remove any white spaces and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted strings are equal
    return sorted(str1) == sorted(str2)

# Test the function
print(are_anagrams("Listen", "Silent"))  # Expected output: True
print(are_anagrams("Hello", "World"))  # Expected output: False

def are_anagrams_count(str1, str2):
    # Remove any white spaces and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count characters
    count = {}

    # Count characters in str1
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtract counts for characters in str2
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            return False

    # Check if all counts are zero
    for k in count:
        if count[k] != 0:
            return False

    return True

# Test the function
print(are_anagrams_count("Listen", "Silent"))  # Expected output: True
print(are_anagrams_count("Hello", "World"))  # Expected output: False