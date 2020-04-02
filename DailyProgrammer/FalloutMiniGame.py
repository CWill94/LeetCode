# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:04:59 2020

@author: Clayton

[2015-10-28] Challenge #238 [Intermediate] Fallout Hacking Game
Description
The popular video games Fallout 3 and Fallout: New Vegas have a computer "hacking" minigame where the player must correctly guess the correct password from a list of same-length words. Your challenge is to implement this game yourself.

The game operates similarly to the classic board game [Mastermind](http://en.wikipedia.org/wiki/Mastermind_(board_game)). The player has only 4 guesses and on each incorrect guess the computer will indicate how many letter positions are correct.

For example, if the password is MIND and the player guesses MEND, the game will indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE and the player guesses PLAYFUL, the game will report 0/7. While some of the letters match, they're in the wrong position.

Ask the player for a difficulty (very easy, easy, average, hard, very hard), then present the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. More words and letters make for a harder puzzle. The player then has 4 guesses, and on each incorrect guess indicate the number of correct positions.

Here's an example game:

Difficulty (1-5)? 3
SCORPION
FLOGGING
CROPPERS
MIGRAINE
FOOTNOTE
REFINERY
VAULTING
VICARAGE
PROTRACT
DESCENTS
Guess (4 left)? migraine
0/8 correct
Guess (3 left)? protract
2/8 correct
Guess (2 left)? croppers
8/8 correct
You win!
You can draw words from our favorite dictionary file: enable1.txt. Your program should completely ignore case when making the position checks.

There may be ways to increase the difficulty of the game, perhaps even making it impossible to guarantee a solution, based on your particular selection of words. For example, your program could supply words that have little letter position overlap so that guesses reveal as little information to the player as possible.

Credit
This challenge was created by user /u/skeeto. If you have any challenge ideas please share them on r/dailyprogrammer_ideas and there's a good chance we'll use them.
"""
import random 
import sys
ATTEMPTS = 4
def main():
    mastergamewords = dictionaryload()
    difficulty = int(input("Please enter a difficulty 1-5: "))
    
    if(difficulty == 1):
        gamewords = dictsplit(mastergamewords,4)
    elif(difficulty ==2):
        gamewords = dictsplit(mastergamewords,5)
        
    elif(difficulty ==3):
        gamewords = dictsplit(mastergamewords,6)
        
    elif(difficulty ==4):
        gamewords = dictsplit(mastergamewords,8)
    else:
        gamewords = dictsplit(mastergamewords,10)
        
    gameload(difficulty, gamewords)




#loads masteset list into a list
def dictionaryload():
    with open("enable1.txt") as f:
        words = list(map(lambda s: s.strip().lower(), f.readlines()))
        return words
#gets a subset of words matching a length based on difficulty    
def dictsplit(wordlist, num):
    modlist = filter(lambda x: len(x)==num, wordlist)
    return list(modlist)

#maingame fxn
def gameload(difficulty, words):
 
    setlist = random.sample(words, k=4)
    gameword = random.choice(setlist)
    for words in setlist:
        print(words)
    checkword(gameword, ATTEMPTS)
    if(input("Would you like to play again? y/n : ") == "y"):
        main()
    else:
        sys.exit()
    
    

def checkword(actual, attempts):
    if(attempts == 0):
        return print("You have run out of tries!")
    
    userinput = input("Try to guess the word: ")
    if(userinput == actual):
       return print("You guessed correctly!")
    else:
        correct = 0
        for i in range(len(actual)):
            if(userinput[i] == actual[i]):
                print(userinput[i])
                print(actual[i])
                correct += 1
                print(correct)
        print("You have guessed %d out of %d correctly" %(correct, len(actual)))
        attempts -= 1
        print("You have %d guesses remaining" %attempts)
        checkword(actual, attempts)
main()

    
    
    