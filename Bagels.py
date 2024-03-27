"""Bagels, by Al Sweigart a;@inbentwith python.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-pyton-projects
A version of this game is featured in teh book "Invent Your Own Computer Games wit Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 #Try setting to another number
MAX_GUESSES = 10 #Try setting to another number

def main():
    print('''Bagels, a deductive logic game. 
By Al Sweigart.
I am thinking of a []-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
Pico:       One digit is correct but in the wrong position.
Fermi:      One digit is correct and in the right position.
Bagels:     No digit is correct.
          
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi, Pico.'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or guess.isdecimal() != True:
                print("Guess #{}:".format(numGuesses))
                guess = input(">")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print("You win!")
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")
    

def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
        if len(clues) == 0:
            return "Bagels"
        else:
            clues.sort()
            return ' '.join(clues)
        
main()
