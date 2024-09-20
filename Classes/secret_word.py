secret_word = "giraffe"
guess = ""
guess_count= 0
guess_limit =3
i =0
while i< 4:
    i+=1
    while guess != secret_word:
        guess = input("Enter Guess: ")
        
print("Maximum Trial Period Exceeded")


print("You Win ")

