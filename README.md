# HANGMAN
#### Video Demo:  [URL](https://www.youtube.com/watch?v=39JqgG2PhG0)

## __Definition__
This project allows a user to play a hangman game where they input the initial word to guess.

Project Structure:
- project.py
- test_project.py
- requirements.txt
- README.md

## __Libraries__
pyfiglet: a full port of figlet into python that takes ASCII Art and renders it in ASCII art fonts ([Readmore](https://pypi.org/project/pyfiglet/)).

## __Installing Libraries__
To install pyfiglet, simply run the command:
> pip install pyfiglet

## __Usage__
When running project.py, the user is prompted with the following:

```python project.py```
```
 _       __     __                             __
| |     / /__  / /________  ____ ___  ___     / /_____
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/

    __  __                                        __
   / / / /___ _____  ____ _____ ___  ____ _____  / /
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \/ /
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /_/
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_(_)
                  /____/

Enter Word:
```
After that, the user enters the word they would want another player to guess. Before the game starts, the number of blanks corresponding to the number of letters in the word print accordingly.

```
Enter Word: Hello
 _ _ _ _ _
```

The user must enter a letter one a time either uppercase or lowercase.

 If users guesses a letter that has already been guessed, the user is prompted again:
 ```
h _ _ _ _
Enter guess: H
Already Guessed!
```
 If the user guesses incorrectly 6 times - they lose the game:

 ```
__  __               ____      _ __         __   __
\ \/ /___  __  __   / __/___ _(_) /__  ____/ /  / /_____
 \  / __ \/ / / /  / /_/ __ `/ / / _ \/ __  /  / __/ __ \
 / / /_/ / /_/ /  / __/ /_/ / / /  __/ /_/ /  / /_/ /_/ /
/_/\____/\__,_/  /_/  \__,_/_/_/\___/\__,_/   \__/\____/

                                  __  __                 _       __    __
   ____ ___  _____  __________   / /_/ /_  ___     _____(_)___ _/ /_  / /_
  / __ `/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / ___/ / __ `/ __ \/ __/
 / /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /  / / /_/ / / / / /_
 \__, /\__,_/\___/____/____/   \__/_/ /_/\___/  /_/  /_/\__, /_/ /_/\__/
/____/                                                 /____/
                          __
 _      _____  _________/ /
| | /| / / __ \/ ___/ __  /
| |/ |/ / /_/ / /  / /_/ /
|__/|__/\____/_/   \__,_/
```
If the user manages to guess the word correctly before getting 6 attempts wrong:
```
__  __                                                   __   __  __
\ \/ /___  __  __   ____ ___  _____  _____________  ____/ /  / /_/ /_  ___
 \  / __ \/ / / /  / __ `/ / / / _ \/ ___/ ___/ _ \/ __  /  / __/ __ \/ _ \
 / / /_/ / /_/ /  / /_/ / /_/ /  __(__  |__  )  __/ /_/ /  / /_/ / / /  __/
/_/\____/\__,_/   \__, /\__,_/\___/____/____/\___/\__,_/   \__/_/ /_/\___/
                 /____/
         _       __    __                             ____
   _____(_)___ _/ /_  / /_   _      ______  _________/ / /
  / ___/ / __ `/ __ \/ __/  | | /| / / __ \/ ___/ __  / /
 / /  / / /_/ / / / / /_    | |/ |/ / /_/ / /  / /_/ /_/
/_/  /_/\__, /_/ /_/\__/    |__/|__/\____/_/   \__,_(_)
       /____/

```
The program terminates after the word is successfuly guessed, or 6 wrong attempts.

## __Functioning__
The project.py contains 3 functions including the main function.

### hangman(word)
Takes in one paramter:
- word: the word to be guessed during the game

After taking the word inputted by the user, the function initializes the following variables:
- guess_letter: used to keep track of letters the user has guessed before.
- incorrect_guess: used to keep track of incorrect letters that the user has guessed.
- i: The number of wrong attempts remaining before the program terminates

The function uses a loop where essentially, as long as i > 0, the loop will run whichever code within. It first initializes the guess variable, which prompts the user to guess a letter. It checks if the user enters a single valid letter. If the user guesses a letter that has already been guessed, the loop runs again prompting the user to enter another guess.

If the user enters a new guess, it checks if the guessed letter is in the word. If it does, the guessed letter is added to the guess_letter list. It also calls the letter_check function, and prints the return value.

If the user enters a new guess, and not in the word to be guessed, the program tells the user it's wrong, and lowers the variable i - which counts the number of attempts down.

If i has reached 0 (which means they guessed 6 letters wrong), the program quits, and says what the word actually was.


### letter_check(word,guess_words)
Takes in two paramters:
- word : word to be guessed
- guess_letter : list of letters attempted

Utilizing a for loop, an individual letter is passed through and compared to every letter in the word to be guessed. For each character position (say the first 1), if the character matches, the letter is appended to the check list. If the letter doesn't match, "_" is appended to the check list. The function itself returns the check list as a single word string.
### end_game(attempt,word)
Takes in two paramters:
- attempt: Fully concatenated word of letters and underscores, or just letters
- word: word to be guessed

This function checks to see if the user manages to guess the correct word. While called in main - every single attempt is checked to see if it matches with the word to be guessed. This is utilized to terminate the program early after the word was successfully guessed or if they run out of attempts.
