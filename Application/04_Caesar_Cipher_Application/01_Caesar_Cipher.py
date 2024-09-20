# Caesar Cipher in Python

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""  # Stores the result (ciphertext or plaintext)
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Find the position of the character in the alphabet (0-25)
            # Apply the shift and use modulo 26 to wrap around if needed
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Check if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # If it's not a letter (like spaces or punctuation), add it unchanged
        else:
            result += char

    return result

# Example usage
plaintext = "Hello World!"
shift = 3

# Encrypting
ciphertext = caesar_cipher(plaintext, shift, mode='encrypt')
print(f"Encrypted: {ciphertext}")

# Decrypting
decrypted_text = caesar_cipher(ciphertext, shift, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
