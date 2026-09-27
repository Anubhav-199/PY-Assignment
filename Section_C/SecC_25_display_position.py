"""
Section C - Q25: Print Characters with Position
Concepts: range(), indexing

Example:
Input: JAVA
Output:
Position 0 : J
Position 1 : A
Position 2 : V
Position 3 : A
"""


def display_position(text):
    for i in range(len(text)):
        print(f"Position {i} : {text[i]}")


if __name__ == "__main__":
    text = input("Enter a string: ")
    display_position(text)
