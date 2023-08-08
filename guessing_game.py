"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.
def start_game():
# Write your code inside this function.
    print("Welcome Challenger!")
    randnum = random.randrange(1, 10)
    guess = int(input("Pick a number between One and Ten. "))
    guess_count = 1
    while guess != randnum:
        guess_count += 1
        if guess < randnum:
            print("Guess is too low! ")
        elif guess > randnum:
            print("Guess is too high! ")
        
        
    

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.