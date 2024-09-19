is_male = True
is_tall = True

# if  is_male or is_tall:  # This would work when one or both value is True
#     print("You are a male or tall or both")
    
# else:
#     print("You are neither make nor tall")


# is_female = True
# is_she_tall = True
  
# if is_female and is_she_tall:
#     print("You are a female and you are tall")
# else:
#     print("You are neither a female nor you are tall")



if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")


# IF ELSE STATEMENTS AND COMPARISON OPERSTORS

#=============================================

def max_num(num1, num2, num3):
    if num1 >= num2 and  num1 >= num3:
       return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 4, 5))    