secretWord = str(input("Enter the secret word: "))
lettersGuessed = input ("Enter a list of guessed letters: ")

def isWordGuessed (secretWord, lettersGuessed):
    letter = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        return True
print (isWordGuessed(secretWord, lettersGuessed))
        
    