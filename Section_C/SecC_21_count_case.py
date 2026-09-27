"""
Section C - Q21: Count Uppercase and Lowercase Characters

Example:
Input: Python123 ABC
Uppercase : 3
Lowercase : 6
Digits : 3
Spaces : 1
"""


def count_case(text):
    upper = lower = digits = spaces = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
    print(f"Uppercase : {upper}")
    print(f"Lowercase : {lower}")
    print(f"Digits : {digits}")
    print(f"Spaces : {spaces}")


if __name__ == "__main__":
    text = input("Enter a string: ")
    count_case(text)
