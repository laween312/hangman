#name= input("enter single letter")
#name = guess
#guess=input("enter single letter")

#create an if statement that checks if the length of the input is equal to 1 and the input is an alphabet.

# In the body of the if statement, print a message that says "Good guess!".

# Create an else block that prints "Oops! That is not a valid input." if the preceeding conditions are not met.




guess = input("can you guess a letter")
if len("guess")==1 and guess.isalpha():
    print("good guess")   
else:
    print("Oops! That's not a valid input.")










import random


#pass word_list into choice
word_list = ["banana","apple","oranges","pears","watermelon"]
word = random.choice(word_list)
print(word)
print(word_list)

