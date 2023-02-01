import random 
word_list = ["banana","apple","oranges","pears","watermelon"]
print (word_list) 

word = random.choice(word_list)
guess = input("please guess a letter")
while True:
    guess = input("please guess a letter")
    
    if len("guess")==1 and guess.isalpha():
        print ("Good guess")
        break  
    else:
        print("Invalid letter. Please, enter a single alphabetical character.") 
       
        #Create an if statement that checks if the guess is in the word.

# In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

# Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
        
    if guess in word:
     print ("Good guess! {guess} is in the word.")
    else:
     print ("Sorry, {guess} is not in the word. Try again.")    
     
     import random
     
     word_list =  ["banana","apple","oranges","pears","watermelon"]
     
     def check_guess(guess):
          ask_for_input
          guess.lower
         
        
    if guess in word:
     print ("Good guess! {guess} is in the word.")
    else:
     print ("Sorry, {guess} is not in the word. Try again.")  
     
     def ask_for_input():
         while True:
             guess = input ("guess a letter")
             check_guess(guess)
             if (guess.isalpha() ==  True) and (len(guess) ==1):
                 break
             else:
              print("invalid letter. Please enter a single alphabetical charcater")
              break
             return ask_for_input()
         #ask_for_input
      
      
