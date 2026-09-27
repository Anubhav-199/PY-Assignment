"""
Section B - Q18: Find Frequency of a Character
Restriction: Do not use count().

Example:
Text : programming
Character : g
Frequency : 2
"""


def character_frequency(text, ch):
    frequency = 0
    for c in text:
        if c == ch:
            frequency += 1
    return frequency


if __name__ == "__main__":
    text = input("Enter a string: ")
    ch = input("Enter a character to search: ")
    print(f"Frequency of '{ch}' = {character_frequency(text, ch)}")
