#Create a while loop and set the condition to True. Setting the condition to True ensures that the code run continuously. In the body of the loop, write the code required for the following steps.

# Ask the user to guess a letter and assign this to a variable called guess.

# Check that the guess is a single, alphabetical character.

# If the guess passes the checks, break out of the loop.

# If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
import random
word_list = ["banana","apple","oranges","pears","watermelon"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input('Guess a single letter: ')
        
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    
    
    



