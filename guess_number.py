#guess_number.py
#Date: 24/September/2020
#by irving-rs

#Description:
#Guess The Secret Number: A game in which the user tries to find the secret number.

#Basics:
#The computer selects an aleatory number (secret number) between 0 and 99.
#The user has to discover the secret number.
#The user has 7 opportunities to guess the secret number.

#Preparatives:
from random import randrange #Needed to perform the aleatory selection.

#Functions:
def result(secret_n, sel_user): #Checks if the guess is rigth "True" , or wrong "False"
    if secret_n == sel_user: #If the guess is rigth.
        print("\nCongratulations, your guess is rigth!\n")
        return True
    elif secret_n > sel_user: #If the secret number is major than the guess number.
        print("\nWrong: The secret number is higher.\n")
        return False
    else: #If the secret number is minor than the guess number.
        print("\nWrong: The secret number is lower.\n")
        return False

#Variables:
escape = False #To control while loop.
i = 0 #Counter

#Presentation of the game:
print("\nGuess The Secret Number:\n")

#Rules:
print("Rules:")
print("1. The secret number is an integer between 0 and 99.")
print("2. You have to discover the secret number.")
print("3. You only have 7 opportunities.")
print("\nAdvice: Follow the tips.\n")

#Main body:

secret_n = randrange(0,100) #Secret number generation.

while (escape == False):
    i += 1 #Counter
    print("Opportunity:", i) #Number of opportunities. 
    sel_user = int(input("Your guess: ")) #User selection.

    if result(secret_n, sel_user) == True: #If the guess is rigth.
        escape = True #To escape from while loop.
    elif i == 7: #If the guess is wrong and it was the last chance.
        print("Sorry, you have lost.")
        print("The secret number was:", secret_n, "\n")
        escape = True #To escape from while loop.
