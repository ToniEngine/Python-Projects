score =int(input("Score: "))

if score >=70 and score <=100:
    print("You have an A")
elif score >=60 and score <70:
    print("You have a B")
elif score >=50 and score <60:
    print("You have a C")
elif score >=45 and score <50:
    print("You have a D")
elif score <45:
    print("Opps You have an F")
else:
    print("Sorry! Grade does not exist")