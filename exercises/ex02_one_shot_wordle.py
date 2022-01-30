"""EX02 - One-Shot Wordle."""

__author__ = "730484959"

secret_word: str = "python"
checking_indices: int = 0
guess_emojis = " "

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


user_inputed_word: str = input(f"What is your {len(secret_word)}-letter guess? ")


while len(user_inputed_word) != len(secret_word):
    user_inputed_word = input(f"That was not {len(secret_word)} letters! Try again: ")

while checking_indices < len(secret_word):
    if user_inputed_word[checking_indices] == secret_word[checking_indices]:
        guess_emojis = guess_emojis + GREEN_BOX
    else:
        yellow_characters: bool = False
        alternate_indices = 0
        while yellow_characters is not True and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == user_inputed_word[checking_indices]:
                yellow_characters = True
            else:
                alternate_indices = alternate_indices + 1
        if yellow_characters is True:
            guess_emojis = guess_emojis + YELLOW_BOX
        else:
            guess_emojis = guess_emojis + WHITE_BOX
    checking_indices += 1
print(guess_emojis)

if user_inputed_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")