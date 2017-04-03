import string
import random
import os

os.system("clear")

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    a = 0
    lst = list(secretWord)
    for i in lettersGuessed:
        while(True):
            if i in lst:
                count+=1
                a = lst.index(i)
                lst[a] = '0'
            else:
                break
    if count == len(secretWord):
        return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    lst = list(secretWord)
    for i in lst:
        if i not in lettersGuessed:
            lst[lst.index(i)] = '_'
    return " ".join(lst)


def getAvailableLetters(lettersGuessed):
    avl = list(string.ascii_lowercase)
    for i in lettersGuessed:
        avl.remove(i)
    return "".join(avl)

def hangman(secretWord):
    count = 8
    flag = 0
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d letters long." % (len(secretWord)))
    print("------------")
    while(count!=0):
        print("You have %d guesses left." % (count))
        print("Available letters: %s" % (getAvailableLetters(lettersGuessed)))
        a = input("Please guess a letter: ")
        if(a.lower() not in list(getAvailableLetters(lettersGuessed))):
            print("Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            continue
        lettersGuessed = lettersGuessed + [a.lower()]
        if(a.lower() in list(secretWord)):
            print("Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed)))
        else:
            count-=1
            print("Oops! That letter is not in my word: %s" % (getGuessedWord(secretWord, lettersGuessed)))
        print("------------")
        if isWordGuessed(secretWord, lettersGuessed):
            flag = 1
            break
    if(flag):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was %s." % (secretWord))
        

secretWord = chooseWord(loadWords()).lower()
hangman(secretWord)