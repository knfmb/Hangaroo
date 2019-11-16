import string
import random

wordstoguess = ["mouse", "frame", "basketball", "subido", "tigers", "coldplay", "clock",
            "perfume", "lipstick", "pistachio", "cheerdance"]

secretWord = random.choice (wordstoguess)


def isWordGuessed (secretWord, lettersGuessed):
    letter = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        return True
    
def getGuessedWord(secretWord,lettersGuessed):
    undscore = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            undscore = undscore + letter
        else:
            undscore = undscore + "_ "
    return undscore

def getAvailableLetters (lettersGuessed):
    lcletters = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in lcletters:
            lcletters = lcletters.replace(letter,"")
    return lcletters

def Hangaroo(secretWord):
    length = len(secretWord)
    lettersGuessed = []
    guesstheword = False
    attempts = 4
    hula = str
    
    print ("\nHello friend and welcome to Hangaroo!")
    print ("Wanna relieve some stress?")
    print ("Come and let's play a game!\n\n")
    print ("You will need to guess the word I am thinking of. Ready?")
    print ("\nThe word is ", length, " letters long.\n")
    
    
    while attempts > 0 and attempts <= 4 and guesstheword is False:
        if secretWord == getGuessedWord(secretWord,lettersGuessed):
            guesstheword = True
            break
        
        print ("You have ", attempts, " attempts left.")
        print ("The available letters are: ", getAvailableLetters (lettersGuessed))
        hula = input ("Please input a letter: ").lower()
        
        if hula in secretWord:
            if hula in lettersGuessed:
                print ("This letter has been used. Try another letter.")
            else:
                lettersGuessed.append(hula)
                print ("Great!")
                print (getGuessedWord(secretWord,lettersGuessed))
        
        else:
            if hula in lettersGuessed:
                print ("This letter has been used. Try another letter.")
            else:
                lettersGuessed.append(hula)
                attempts = attempts - 1
                print ("The letter you entered is incorrect.")
    if guesstheword == True:
        return "Congratulations! You suceeded."
    elif attempts == 0:
        print ("Unable to guess the word. The word was ", secretWord)
    
               