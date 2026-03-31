# ord : ord function is used to get the ASCII value of a character. It takes a single character as an argument and returns its ASCII value.
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97

# ASCII value of space character is 32
print(ord(' '))  # Output: 32

print(ord('d'))




# chr : chr function is used to get the character corresponding to an ASCII value. It takes an integer as an argument and returns the character corresponding to that ASCII value.
print(chr(65))  # Output: 'A'
print(chr(97))  # Output: 'a'
print(chr(32))  # Output: ' '
print(chr(100)) # Output: 'd'

# we can also use ord and chr functions together to convert a character to its ASCII value and then back to the character.
char = 'B'
ascii_value = ord(char)  # Get ASCII value of 'B'
print(ascii_value)  # Output: 66    

# Convert ASCII value back to character
character = chr(ascii_value)


# ASCII stands for American Standard Code for Information Interchange. It is a character encoding standard that assigns a unique numeric value to each character, including letters, digits, punctuation marks, and control characters. The ASCII values range from 0 to 127, where each value corresponds to a specific character. For example, the ASCII value of 'A' is 65, 'a' is 97, and space is 32. ASCII is widely used in programming and data processing to represent text and control characters in a standardized way.

