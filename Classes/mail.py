# Initialize an empty list to store the emails
email_list = []

while True:
    first_name = input("What is your first name? ")
    
    # Check if there's no space in the first name
    if " " not in first_name:
        print(f"Hello, {first_name}. Enter your last name below.")
        last_name = input("What is your last name? ")
        
        print(f"Hello {first_name} {last_name}, please enter the name of your company below.")
        company_name = input("Enter Company name: ")
        
        # Create customized email address
        email = f"{first_name.lower()}{last_name.lower()}@{company_name.lower()}.com"
        print(f"Your Company Customized email is {email}")
        
        # Store the generated email in the email list
        email_list.append(email)
        
        # Ask if user wants to generate another email
        another = input("Would you like to generate another email? (yes/no): ").lower()
        if another != 'yes':
            break  # Exit the loop if the user doesn't want to generate more emails
    
    # If there's a space in the first name
    else:
        print("Error! The Company needs your first name without spaces.")
        continue  # Ask for the first name again

# Print all the stored emails at the end
print("\nAll Generated Emails:")
for e in email_list:
    print(e)
