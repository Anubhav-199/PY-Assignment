"""
Section B - Q16: Check Palindrome String

Example:
madam -> Palindrome
hello -> Not Palindrome
"""


def check_palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        print(f"{text} -> Palindrome")
    else:
        print(f"{text} -> Not Palindrome")


if __name__ == "__main__":
    text = input("Enter a string: ")
    check_palindrome(text)
