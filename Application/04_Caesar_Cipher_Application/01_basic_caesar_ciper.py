message = "Hello, World!"
shift = 7

result =""

for char in message:
    char_code = ord(char)
    new_char_code = shift + char_code
    new_char = chr(new_char_code)

    result += new_char

    # print(char, char_code, new_char_code, new_char)
    print(result)
print(result)