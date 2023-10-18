print("Type help to view all the commands.")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("The car is already Started...")
        else:
            started = True
            print("Car Started")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == 'help':
        print(""" 
Start -  To Start the car.
Stop  -  To stop the car.
Quit  -  To quit.
              """)
    elif command == 'quit':
        print("Byee,See you again..............")
        break
    else:
        print("Sorry I don't Understand.")
        
        
        