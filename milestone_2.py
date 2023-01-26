#Create a file named milestone_2.py. This file will contain the code for the first milestone. In Python, Lists are used to store multiple data in a single variable. In this task, we are going to create a list of words.

# Create a list containing the names of your 5 favorite fruits.

# Assign this list to a variable called word_list.

# Print out the newly created list to the standard output (screen).

#def list of fruits as word_list
word_list = ["banana","apple","oranges","pears","watermelon"]
print (word_list) 




name= input("enter single letter")
#name = guess
guess=input("enter single letter")

#create an if statement that checks if the length of the input is equal to 1 and the input is an alphabet.

# In the body of the if statement, print a message that says "Good guess!".

# Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.

import random


#pass word_list into choice
word_list = ["banana","apple","oranges","pears","watermelon"]
word = random.choice(word_list)
print(word)
print(word_list)


guess = input("can you guess a letter")
if len("guess")==1 and guess.isalpha():
    print("good guess")   
else:
    print("Oops! That's not a valid input.")
    
#Write code that will continuously ask the user for a letter and validate it.

#Create a new script called milestone_3.py. This file will contain the code for this milestone.

#Step 1. Create a while loop and set the condition to True. Setting the condition to True ensures that the code run continuously. In the body of the loop, write the code required for the following steps.

#Step 2: Ask the user to guess a letter and assign this to a variable called guess.

#Step 3. Check that the guess is a single, alphabetical character.

#Step 4. If the guess passes the checks, break out of the loop.

#Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."


guess = input("please guess a letter")
while True:
    guess = input("please guess a letter")
    
    if len("guess")==1 and guess.isalpha():
     print ("Good guess")
    break
else:
    print("Invalid letter. Please, enter a single alphabetical character.")
    


# Create an if statement that checks if the guess is in the word.

#In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

#Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

import random 
word_list = ["banana","apple","oranges","pears","watermelon"]

  
if guess in word:
     print("Good guess! {guess} is in the word.")
else:
     print("Sorry, {guess} is not in the word. Try again.")
     
     # define a function called check_guess, pass in the guess a parameter for the function
     #convert the guess into a lower case
     #
     
     
     import random 
word_list = ["banana","apple","oranges","pears","watermelon"]
def check_guess(guess):
   guess = guess.lower()
    
if guess in word:
     print(f"Good guess! {guess} is in the word.")
else:
     print(f"Sorry, {guess} is not in the word. Try again.")
     
     def ask_for_input():
         while True:
          guess = input("please guess a letter")
    
     if len("guess")==1 and guess.isalpha():
      print ("Good guess")
      
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")
     
     check_guess(guess)
     
     
     
     #ask_for_input()
    


     