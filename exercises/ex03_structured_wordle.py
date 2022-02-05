"""EX03 - A structured wordle."""

__author__ = "730484959"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """When given two strings, it checks if the letter is in the word."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        else:
            i += 1
    return False
   

def emojified(guess: str, secret: str) -> str:
    """Given a guess, it returns an emoji that shows how close it is to the secret word."""
    assert len(guess) == len(secret)
    guess_emoji: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]: 
            guess_emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                guess_emoji += YELLOW_BOX
            else: 
                guess_emoji += WHITE_BOX
        i += 1
    return guess_emoji


def input_guess(expected_length: int):
    """Prompts the user for a guess that meets the expected length."""
    user_inputed_word = input(f"Enter a {expected_length} character word: ")
    while len(user_inputed_word) != expected_length:
        user_inputed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_inputed_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    win: bool = False 
    while turns != 7 and win is False:
        print(f"=== Turn {turns}/6")
        user_inputed_word: str = input_guess(len(secret))
        print(emojified(user_inputed_word, secret))
        if user_inputed_word == secret:
            win = True
            print(f"You won in {turns}/6 turns!")
        else:
            turns += 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()