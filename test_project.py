import pytest

from project import hangman, letter_check, end_game


def test_correct_hangman(monkeypatch):

    responses = ['h', 'e', 'l', 'a', 'a', 'o']

    input_gen = (response for response in responses)

    monkeypatch.setattr('builtins.input', lambda _: next(input_gen))

    assert hangman("hello") == 'hello'

def test_wrong_hangman(monkeypatch):

    responses = ['a', 'b', 'c', 'd', 'e','f','g']

    input_gen = (response for response in responses)

    monkeypatch.setattr('builtins.input', lambda _: next(input_gen))

    # Test hangman function
    assert hangman("hi") == ''


def test_letter_check():
    assert letter_check("hello","h") == 'h _ _ _ _'
    assert letter_check("hEllo","e") == ' _e _ _ _'
    assert letter_check("hEllo","L") == ' _ _ll _'

def test_end_game():
    assert end_game("h_ello","hello") == 'You failed to guess the right word'
    assert end_game("h_____","hello") == 'You failed to guess the right word'
    assert end_game("hello","hello") == 'You guessed the right word!'
    assert end_game("CoMpUtEr","computer") == 'You guessed the right word!'

