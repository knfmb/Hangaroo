import string
lettersGuessed = input ("Enter a list of guessed letters: ")

def getAvailableLetters (lettersGuessed):
    lcletters = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in lcletters:
            lcletters = lcletters.replace(letter,"")
    return lcletters
    
print (getAvailableLetters(lettersGuessed))