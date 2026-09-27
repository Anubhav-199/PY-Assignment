"""
Section C - Q22: Find First Character
Restriction: Do not directly use text[0]. Use a loop and break.
"""


def first_character(text):
    for ch in text:
        print(f"First character: {ch}")
        break


if __name__ == "__main__":
    text = input("Enter a string: ")
    first_character(text)
