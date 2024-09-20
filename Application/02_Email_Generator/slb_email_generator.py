'''This Program gets the First and Last name of slb new employees and uses
 the first letter of their first name in capital and titled case of their last name and generate 
 a company email for them'''



while True:
    first_name = input("What is your first name? \n")
    index_first_name =first_name[0]
    # print(index_first_name)
    if " " not in first_name:
        print(f"Hello, {first_name}, enter your last name below")
        last_name = input("What is your last name? \n")
        if " "  in last_name:
           print("Error! The Company needs your first name without spaces")
        else:
            title_last_name = last_name.title()
            # print(title_last_name)
            print("Hello " + first_name + " " + last_name +"," + "Please enter the name of your company below")
            company_email_list = [" ",]
            company_name = input("Enter Company name ")
            email = index_first_name.upper()+title_last_name
            customised_email = email +"@"+ company_name.lower()
            # email_list = first_name +" " + last_name, customised_email
            # list_store =company_email_list.append(customised_email)

            
            # company_email_list += list_store

            print(company_email_list)        
            print(customised_email)
            # print(list_store)
            # print(dict(email_list))
            print(f"Your  Customised Company email is {customised_email}.com")
            quit()
   
# elif " " in first_name:
    else:
     print("Error! The Company needs your first name without spaces")
    continue
    