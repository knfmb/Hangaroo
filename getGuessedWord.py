secretWord = str(input("Enter the secret word: "))
lettersGuessed = input ("Enter a list of guessed letters: ")

def getGuessedWord (secretWord, lettersGuessed):
    undscore = " "
    for letter in secretWord:
        if letter in lettersGuessed:
            undscore = undscore + letter
        else:
            undscore = undscore + "_ "
    return undscore

print (getGuessedWord(secretWord, lettersGuessed))
    