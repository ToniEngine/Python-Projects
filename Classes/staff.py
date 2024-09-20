while True:
    first_name = input("What is your first name? ")
    
    # Check if there's a space in the first name
    if " " not in first_name:
        print(f"Hello, {first_name}. Enter your last name below.")
        last_name = input("What is your last name? ")
        
        print(f"Hello {first_name} {last_name}, please enter the name of your company below.")
        company_name = input("Enter Company name: ")
        
        # Create customized email address
        email = first_name + last_name
        print(f"Your Company Customized email is {email.lower()}@{company_name.lower()}.com")
        
        break  # Exit the loop after successfully generating the email
    
    # If a space is found in the first name
    else:
        print("Error! The Company needs your first name without spaces.")
        continue  # Ask for the first name again
