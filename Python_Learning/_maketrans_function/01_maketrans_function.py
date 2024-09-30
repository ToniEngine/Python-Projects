
# maketrans() function and translate() method
'''
The maketrans() function returns a translation table that
can be used by the translate() method to replace the specified characters in a string. 
The translate() method replaces each character in the input string that matches a key 
in the translation table with the corresponding value
'''
my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)
print(my_string)
print(translated_string)



