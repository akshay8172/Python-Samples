#Rock Paper Scissors Game.
import random
def play_game():
    print("Hey, Let's Play - ROCK PAPER SCISSORS 😉")
    user = int(input(
        "Enter Your Choice :\n * 0 for ROCK\n * 1 for PAPER\n * 2 for SCISSORS\n"))
    print(f"YOU CHOOSES: {user}")
    # Conditions
    if user >= 3 or user < 0:
        print('Invalid Input')
    else:
        computer = random.randint(0, 2)
        print("COMPUTER CHOOSES:", computer,"\nRESULT :")
        if user == computer:
            print(
                f"IT'S A DRAW BECAUSE YOU AND COMPUTER CHOOSE {user} and {computer}")
        elif user == 2 and computer == 0:
            print("YOU LOST 🥲!!!!\n")
        elif user == 0 and computer == 2:
            print('YOU WIN 😁!!!\n')
        elif user > computer:
            print("YOU WON 😁!\n")
        elif computer > user:
            print("YOU LOST 🥲!!!\n")
def main():
    while True:
        play_game()
        game = input("Do you want to play again? (Y/N): ")
        if game.upper() != 'Y':
            print("Thanks for playing! See you next time.....")
            break
        
#This is the main program of rockpaperscissors.  
if __name__ == "__main__": 
    main()