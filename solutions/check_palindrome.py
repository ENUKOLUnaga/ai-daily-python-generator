def check_palindrome(s):
    # remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # compare the string with its reverse
    return s == s[::-1]

# test the function
print(check_palindrome("radar"))  # True
print(check_palindrome("hello"))  # False
print(check_palindrome("A man a plan a canal Panama"))  # True
print(check_palindrome("Not a palindrome"))  # False