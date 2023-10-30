import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. Attempts remaining:", attempts)
            if attempts == 0:
                print("You're out of attempts. The word was:", word)
                break

        word_display = display_word(word, guessed_letters)
        print(word_display)

        if "_" not in word_display:
            while True:
                play_again = input("Congratulations! You've guessed the word. Would you like to play again? (Y/N): ").lower()
                if play_again == "y":
                    hangman()
                    break
                elif play_again == 'n':
                    print("Thanks for playing!")
                    break
                else:
                    print("Please enter 'Y' or 'N'.")
            break

if __name__ == "__main__":
    hangman()
