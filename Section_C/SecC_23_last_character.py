"""
Section C - Q23: Find Last Character
Restriction: Demonstrate text[-1] and a loop-based approach.
"""


def last_character_indexing(text):
    return text[-1]


def last_character_loop(text):
    last = ""
    for ch in text:
        last = ch
    return last


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Last character (indexing) : {last_character_indexing(text)}")
    print(f"Last character (loop)     : {last_character_loop(text)}")
