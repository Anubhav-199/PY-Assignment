"""
Section C - Q24: Print Each Character

Example:
Input: PYTHON
Output:
P
Y
T
H
O
N
"""


def display_characters(text):
    for ch in text:
        print(ch)


if __name__ == "__main__":
    text = input("Enter a string: ")
    display_characters(text)
