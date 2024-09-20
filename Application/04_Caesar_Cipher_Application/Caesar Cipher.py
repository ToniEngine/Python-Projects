message = "Hello, World"

for char in message.upper():
    print(f"This is char:{char}")

to_know_first_char = ord("A")
print(to_know_first_char)

# print(ord(""))

def to_know_char():
    user_input = input("Enter the Letter you want to know the Ascii Value ")
    convert_input = ord(user_input)
    print(f"The ASCII Value of, {user_input}, is:, {convert_input}")

to_know_char()