# message = "Hello, World!"
# shift = 7
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE  + 1


def ceasar_shift(message, shift):

    
    result =""

    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)               #Converts Character to ASCII code.
            new_char_code = shift + char_code   #Adds the value of shift and value of ASCII Code together
            
            if new_char_code > LAST_CHAR_CODE:              #to check if the value of the char code exceeds
                new_char_code = new_char_code-CHAR_RANGE    #to loop it back to start from the beginning

            new_char = chr(new_char_code)       #Converts New Value to corresponding ASCII Letter
            result += new_char
        else:
            result += char

    print(result)

user_message = input("Enter Message to Encrypt ")
user_shift_key =int(input("Enter Shift Key(Integer: ) "))
ceasar_shift(user_message, user_shift_key)