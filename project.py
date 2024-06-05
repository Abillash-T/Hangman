from pyfiglet import Figlet



def main():

    f = Figlet(font='slant')
    print(f.renderText("Welcome to Hangman!"))

    while True:
        word = input("Enter Word: ").lower()
        print(len(word) * "_ ")

        if word.isalpha():
            attempt = hangman(word)
            print(f.renderText(end_game(attempt, word)))
            break

        else:
            print("please enter valid word")



def hangman(word):
    guess_letter = []
    incorrect_guess = []
    i = 6
    while i > 0:
        guess = input("Enter guess: ").lower()
        if guess.isalpha():
            if len(guess) == 1:
                if guess in guess_letter or guess in incorrect_guess:
                    print("Already Guessed!")
                else:
                    if guess in word:
                        guess_letter.append(guess)
                        attempt = letter_check(word, guess_letter)
                        print(attempt)
                        if attempt == word:
                            return attempt

                    else:
                        print("Wrong!")
                        
                        incorrect_guess.append(guess)
                        i -=1
            else:
                print("input can only be one character long")
        else:
            print("input must be a letter")

    print("Out of attempts. The word was:", word)
    return ""




def letter_check(word,guess_letter):
    check = []

    for letter in word.lower():
        if any(letter.lower() == guessed_letter.lower() for guessed_letter in guess_letter):

            check.append(letter)
        else:
            check.append(" _")
    return ''.join(check)


def end_game(attempt,word):
    if attempt.lower() == word.lower():
        return "You guessed the right word!"
    else:
        return "You failed to guess the right word"


if __name__ == "__main__":
    main()
