import random

secret_number = random.randint(0, 9)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1

    if guess == secret_number:
        print("You Won !!!")
        break 
    else:
        print("Incorrect guess. Try again.")

if guess_count == guess_limit:
    print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}")
    
print("GAME OVER")
