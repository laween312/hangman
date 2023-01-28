guess = input("please guess a letter")
while True:
    guess = input("please guess a letter")
    
    if len("guess")==1 and guess.isalpha():
        print ("Good guess")
        break  
    else:
        print("Invalid letter. Please, enter a single alphabetical character.") 
       
       #check_guess(guess)
        
        #ask_for_input()
