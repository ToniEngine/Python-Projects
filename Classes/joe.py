name = ''
while True:
    name = input('Who are you? \n')
    lower =name.title()
    if lower != 'joe':
        print('Wrong name, try again.')
        continue  # Go back to the beginning of the loop to ask for the name again

    print(f'Hello {name}, What is the password?')
    password = 'Vinscent01'
    
    # Loop to repeatedly ask for the password if incorrect
    while True:
        user_input = input()
        if user_input == password:
            print('Access Granted')
            break  # Break the inner loop if the password is correct
        else:
            print('Error, try again')
    break  # Exit the outer loop once access is granted
