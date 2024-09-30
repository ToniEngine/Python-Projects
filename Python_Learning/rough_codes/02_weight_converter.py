weight = float(input("Enter Weight: "))
weight_unit = input("(L)bs or (K)g: ")

if weight_unit.upper() == "L":
    converted_weight = weight*0.45
    print(f"You are {converted_weight} kilos")

elif weight_unit.upper()  == "K": 
    converted_weight = weight/0.45
    print(f"You are {converted_weight} pounds")

else:
    print("Invalid Entry")