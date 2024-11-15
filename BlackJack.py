'''Blackjack, by Al Sweigart
"The classic card game also known as 21. (This version doesn't have splitting or insurance.) '''

import random
import sys

#Constants for suit sybols
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print("""Blackjack by Al Sweigart
          
    Rules:
    Try to get as close to 21 wihtout going over.
    Kinngs, Queens, Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth thir face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increaase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.""")

    money = 5000
    while True: 
        #Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()