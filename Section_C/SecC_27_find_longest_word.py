"""
Section C - Q27: Find Longest Word
Restriction: Do not use dictionaries, max(), or advanced collections.
Use loops and string processing.
"""


def find_longest_word(text):
    longest = ""
    current_word = ""
    for ch in text:
        if ch == " ":
            if len(current_word) > len(longest):
                longest = current_word
            current_word = ""
        else:
            current_word += ch
    if len(current_word) > len(longest):
        longest = current_word
    return longest


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(f"Longest word = {find_longest_word(text)}")
