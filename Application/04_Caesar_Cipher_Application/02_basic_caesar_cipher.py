message = "Hello, World!"
shift = 7

result =""

for char in message.upper():
    if char.isalpha():
        char_code = ord(char)               #Converts Character to ASCII code.
        new_char_code = shift + char_code   #Adds the value of shift and value of ASCII Code together
        
        if new_char_code > 90:              #to check if the value of the char code exceeds
            new_char_code = new_char_code-26 #to loop it back to start from the beginning

        new_char = chr(new_char_code)       #Converts New Value to corresponding ASCII Letter
        result += new_char
    else:
        result += char

print(result)