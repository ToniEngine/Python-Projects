text = "Hello World"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""


for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    
    encrypted_text = encrypted_text + alphabet[new_index]
    print(encrypted_text)
print(encrypted_text)