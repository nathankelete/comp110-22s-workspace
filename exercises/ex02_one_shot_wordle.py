"""EX02 - One-Shot Wordle."""

__author__ = "730484959"

secret_word: str = "python"
checking_indices: int = 0
guess_emojis = " "

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Asking user for their guess"""

user_inputed_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

"""Making sure the user types the amount of letters specified"""

while len(user_inputed_word) != len(secret_word): 
    user_inputed_word = input(f"That was not {len(secret_word)} letters! Try again: ")

while checking_indices < len(secret_word):
    """Telling the user which letters are in the correct spot"""
    if user_inputed_word[checking_indices] == secret_word[checking_indices]:
        guess_emojis = guess_emojis + GREEN_BOX
    else:
        yellow_characters: bool = False
        alternate_indices = 0
        while yellow_characters is not True and alternate_indices < len(secret_word):
            """Making note of which letters of the user's word are in the secret word, but in the wrong spot"""
            if secret_word[alternate_indices] == user_inputed_word[checking_indices]:
                yellow_characters = True
            else:
                """Making sure the loop isn't infinite"""
                alternate_indices = alternate_indices + 1
        if yellow_characters is True:
            """Printing which letters specifically are in the wrong spot but in the secret word"""
            guess_emojis = guess_emojis + YELLOW_BOX
        else:
            """Printing which letters are not in the secret word at all"""
            guess_emojis = guess_emojis + WHITE_BOX
    """Making sure the original loop isn't infinite"""
    checking_indices += 1
print(guess_emojis)

if user_inputed_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
