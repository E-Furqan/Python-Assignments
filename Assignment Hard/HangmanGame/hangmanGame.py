import random

word_list = ["python", "hangman", "developer", "computer", "programming", "algorithm"]

def chooseWord():
    return random.choice(word_list)

def displayIncorrectGuesses(incorrect_guesses):
    return f"Incorrect guesses: {', '.join(incorrect_guesses)}"

def displayWord(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangmanVisuals(incorrect_guesses):
    stages = [
        '''
           ------
           |    |
                |
                |
                |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
           ========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
           ========
        '''
    ]
    return stages[len(incorrect_guesses)]
    
def playHangman():
    word = chooseWord()
    guessedLetters = []
    incorrectGuesses = []
    maxIncorrectGuesses = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\nCurrent word: ", displayWord(word, guessedLetters))
        print(hangmanVisuals(incorrectGuesses))
        print(displayIncorrectGuesses(incorrectGuesses))
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessedLetters or guess in incorrectGuesses:
            print("You've already guessed that letter!")
            continue

        if guess in word:
            guessedLetters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrectGuesses.append(guess)
            print(f"Incorrect! '{guess}' is not in the word.")

        if all(letter in guessedLetters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
        
        if len(incorrectGuesses) >= maxIncorrectGuesses:
            print("\nYou've lost! The word was:", word)
            break

def main():
    playHangman()

if __name__=="__main__":
    main()