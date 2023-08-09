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
    guess_count = 1
    
    try:
        guess = int(input("Pick a number between One and Ten. "))
    except ValueError:
        print("Try a number between One and Ten :) ")
    else:
    
        while guess != randnum:
            guess_count += 1
            if guess > 10:
                print("Number was higher than 10")
            elif guess < 1:
                print("Number was lower than 1")
            if guess < randnum:
                guess = int(input("Guess is too low! Try again:  "))
            elif guess > randnum:
                guess = int(input("Guess is too high! Try again:  "))
        if guess == randnum:
            print(f"Winner! It only took you {guess_count} tries! ")
        
       
start_game()
        
        
    

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
