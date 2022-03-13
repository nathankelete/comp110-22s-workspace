def odd_and_evens(list_of_ints: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = 0
    while i < len(list_of_ints):
        if list_of_ints[i] % 2 != 0 and i % 2 == 0:
            new_list.append(list_of_ints[i])
            i += 1 
        else: 
            i += 1
    return new_list


def vowels_and_threes(word: str) -> str:
    i: int = 0
    new_word: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    while i < len(word):
        if word[i] in vowels:
            if i % 3 != 0:
                new_word += word[i]
        else: 
            if i % 3 == 0:
                new_word += word[i]
        i += 1 
    return new_word


