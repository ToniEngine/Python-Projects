def main():
    print_square(3)

def print_square(size):
   #For each row in square
    for i in range(size):
        #For each brick in square
        for j in range(size):
            #Print brick
            print("#", end= "")
        print()
main()