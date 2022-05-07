word = "INCONCEIVABLE"
wordBoard = [' _ '] * len(word)
ATTEMPTS = 5

print("Welcome to hangman terminal eddition. Can you guess the mystery word?")
print("You have 5 attempts.")

def showBoard():
    print(" ".join(wordBoard))


def checkGuess(letter):
    if letter in word:
        startIndex = 0
        for _ in range(word.count(letter)):
            index = word.index(letter, startIndex)
            wordBoard[index] = letter
            startIndex = index + 1
        return True
    else:
        return False


def play():
    currentAttempts = ATTEMPTS
    lettersAlreadyGuessed = []
    showBoard()
    continueGame = True
    while continueGame:
        userGuess = input("Guess a letter: ").upper()
        result = checkGuess(userGuess)

        if result is True:
            print(f"Yes, there is a(n) {userGuess}")
            showBoard()
        elif result is False:
            currentAttempts -= 1
            print(f"I'm sorry but there is no letter {userGuess} in the word.")
            print(f"You have {currentAttempts} attempts left.")
            if userGuess in lettersAlreadyGuessed:
                print("You've already guessed that letter!")
            else:
                lettersAlreadyGuessed.append(userGuess)
                print(f"Letters you've guessed: {lettersAlreadyGuessed}")

        if ' _ ' not in wordBoard:
            continueGame = False
            print("You have guessed the word! Congratulations on winning the game!")
            print(f"The word was {word}")
        else:
            continueGame
        
        if currentAttempts is 0:
            continueGame = False
            print("You ran out of attempts! Game Over!")
            print(f"The word was {word}!")
        else:
            continueGame

play()