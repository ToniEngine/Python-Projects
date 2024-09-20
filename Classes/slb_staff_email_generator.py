"""
This program gets the first and last name of SLB new employees and uses
the first letter of their first name in capital and the titled case of their last name
to generate a company email for them.
"""


company_email_list = []

while True:
    
    first_name = input("What is your first name? \n")
    if " " in first_name:
        print("Error! The Company needs your first name without spaces")
        continue  

    
    index_first_name = first_name[0].upper()

    
    print(f"Hello, {first_name}. Enter your last name below.")
    last_name = input("What is your last name? \n")
    if " " in last_name:
        print("Error! The Company needs your last name without spaces.")
        continue  
    
    
    title_last_name = last_name.title()

    
    print(f"Hello {first_name} {last_name}, please enter the name of your company below.")
    company_name = input("Enter Company name: ")

    
    email = index_first_name + title_last_name
    customised_email = f"{email}@{company_name.lower()}.com"

    
    company_email_list.append(customised_email)
    
    
    print(f"Your Customised Company email is {customised_email}")

    
    another = input("Would you like to generate another email? (yes/no): ").lower()
    if another != 'yes':
        break  


print("\nAll Generated Company Emails:")
for email in company_email_list:
    print(email)
