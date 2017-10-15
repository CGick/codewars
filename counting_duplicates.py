"""
    Count the number of Duplicates

    Write a function that will return the count of distinct
    case-insensitive alphabetic characters and numeric digits
    that occur more than once in the input string. The input
    string can be assumed to contain only alphabets (both
    uppercase and lowercase) and numeric digits.

    Example

    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
    "indivisibility" -> 1 # 'i' occurs six times
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    duplicate = 0
    characters = {}
    for character in text:
        if characters.has_key(character.lower()):
            characters[character.lower()] += 1
        else:
            characters[character.lower()] = 1
    for letter in characters.values():
        if letter > 1:
            duplicate += 1
    print duplicate

if __name__ == '__main__':
    duplicate_count("abcde")
    duplicate_count("abcdea")
    duplicate_count("indivisibility")
    duplicate_count("Mississippim")