"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730484959"

user_inputed_word: str = input("Enter a 5-character word: ")
if len(user_inputed_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_inputed_character: str = input("Enter a single character: ")
if len(user_inputed_character) != 1:
    print("Error: Character must be a single character")
    exit()

number_of_matching_characters: int = 0

print("Searching for " + user_inputed_character + " in " + user_inputed_word)

if user_inputed_word[0] == user_inputed_character:
    print(user_inputed_character + " found at index 0")
    number_of_matching_characters = number_of_matching_characters + 1
if user_inputed_word[1] == user_inputed_character:
    print(user_inputed_character + " found at index 1")
    number_of_matching_characters = number_of_matching_characters + 1
if user_inputed_word[2] == user_inputed_character:
    print(user_inputed_character + " found at index 2")
    number_of_matching_characters = number_of_matching_characters + 1
if user_inputed_word[3] == user_inputed_character:
    print(user_inputed_character + " found at index 3")
    number_of_matching_characters = number_of_matching_characters + 1
if user_inputed_word[4] == user_inputed_character:
    print(user_inputed_character + " found at index 4")
    number_of_matching_characters = number_of_matching_characters + 1

if number_of_matching_characters > 0:
    print(str(number_of_matching_characters) + " instances of " + user_inputed_character + " found in " + user_inputed_word)
else:
    print("No instances of " + user_inputed_character + " found in " + user_inputed_word)