
import random

def guess(x):
    random_no = random.randint(1,x)
    guess = 0
    while random_no != guess:
       guess = int(input(f'Guess the number between 1 to {x}: '))
       
    if guess < random_no:
        print("Guess again.Too low!")
    elif guess > random_no:
        print("Guess again.Too high!")

    print(f"Yay! You have guessed the {random_no} correctly! Truly genius!!")    

guess(10)