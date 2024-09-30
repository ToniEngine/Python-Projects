command = ""
car_is_started = False

while True:
    command =input("> ").lower()
    if command == "start":
        
        if car_is_started:
            print("Car is already started....")
        else:
            car_is_started = True
            print("Car is started")
    elif command == "stop":
        if not car_is_started:
            print("Car is already stopped")
        else:
            car_is_started = False
            print("Car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit  to quit''')
    elif command == "quit":
        break
    else:
        print("Sorry, I do not understand that")
