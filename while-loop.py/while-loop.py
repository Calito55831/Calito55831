#PRINTING THE FAME RULES
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to get it")

#IMPORTING RANDOM AND WRITING A WHILE LOOP
import random
number = random.randint(1,10)
isGuessRight = False 
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. You no sabi book!.".format(guess))
    
    #print("Count to 10!")
    for x in range (0, 11):
        print(x)