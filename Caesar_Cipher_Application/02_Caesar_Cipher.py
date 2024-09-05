message = "Hello, World!"
shift = 7
LAST_CHAR_CODE= 90 #When Vairbles are defined using UPPER CASE LETTERS it signifies that the variables ar constants
CHAR_RANGE = 26

#Store the result in the result variable(placeholder)
result=""


#Create a for loop to loop through the message 
# variable and converting the lower case alpabets to upper case using the .upper method

for char in message.upper():
    if char.isalpha():
        char_code = ord(char) #This converts the character to their respective ASCII values using the ord() function
        new_char_code = char_code + shift
        # print(char_code, new_char_code)

        if new_char_code > LAST_CHAR_CODE:
            new_char = new_char - CHAR_RANGE
        new_char = chr(new_char_code)
        result += new_char 


