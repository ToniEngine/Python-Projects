# Example 1: Using Two Strings
# Create a translation table where 'a' is replaced with '1', 'b' with '2', and 'c' with '3'
trans_table = str.maketrans('abc', '123')
# print(trans_table)  # Output: {97: 49, 98: 50, 99: 51}  why?


# # Original string
text = 'abcde'

# # Apply translation using translate()
translated_text = text.translate(trans_table)

print(translated_text)  # Output: 123de


# ======================================================
# Example 2: Using a Dictionary
# Create a translation table using a dictionary
# Replace 'a' with '1', 'e' with '5', and remove 'i' by mapping it to None
trans_table = str.maketrans({'a': '1', 'e': '5', 'i': None})

# Original string
text = 'alice in wonderland'

# Apply translation using translate()
translated_text = text.translate(trans_table)

print(translated_text)  # Output: 1lc5  n wonderl5nd



# Example 3: Using Three Strings (Removing Characters)
# Create a translation table to replace 'a' with '1', 'b' with '2'
# and remove 'c'
trans_table = str.maketrans('ab', '12', 'c')

# Original string
text = 'abcde'

# Apply translation using translate()
translated_text = text.translate(trans_table)

print(translated_text)  # Output: 12de
